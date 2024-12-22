from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from offers_app.models import Offer, OfferDetail
from .serializers import OfferSerializer, OfferDetailSerializer
from django.db.models import Q
from rest_framework import  viewsets, filters
from .pagination import CustomPageNumberPagination
from .permissions import IsOwnerOrAdmin, IsBusinessProfile


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['updated_at', 'details__price']

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsAuthenticated, IsBusinessProfile]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else: 
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    from django.db.models import Q

    def get_queryset(self):
            queryset = Offer.objects.all()
            user_id = self.request.query_params.get('creator_id')
            min_price = self.request.query_params.get('min_price')
            max_delivery_time = self.request.query_params.get('max_delivery_time')
            search = self.request.query_params.get('search')
            ordering = self.request.query_params.get('ordering', '-updated_at')

            if user_id:
                queryset = queryset.filter(user_id=user_id)

            if min_price:
                try:
                    min_price = float(min_price)
                    queryset = queryset.filter(min_price__gte=min_price)
                except ValueError:
                    pass

            if max_delivery_time:
                try:
                    max_delivery_time = int(max_delivery_time)
                    queryset = queryset.filter(max_delivery_time__lte=max_delivery_time)
                except ValueError:
                    pass  

            if search:
                queryset = queryset.filter(
                    Q(title__icontains=search) | Q(description__icontains=search)
                )

            valid_ordering_fields = ['updated_at', '-updated_at', 'min_price', '-min_price']
            if ordering in valid_ordering_fields:
                queryset = queryset.order_by(ordering)
            else:
                queryset = queryset.order_by('-updated_at')

            return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.pk)
    
    def perform_destroy(self, instance):
        instance.delete()   

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.query_params:
            context['queryset_called'] = True
        else:
            context['queryset_called'] = False
        return context

class OfferDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


