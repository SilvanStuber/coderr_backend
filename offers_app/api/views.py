from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from offers_app.models import Offer, OfferDetail
from .serializers import OfferSerializer, OfferDetailSerializer
from django.db.models import Q
from rest_framework import  viewsets, filters
from .pagination import CustomPageNumberPagination
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .permissions import IsCustomerProfile, IsOwnerOrAdmin


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
            permission_classes = [IsAuthenticated, IsCustomerProfile]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else: 
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):   
        try:
            queryset = Offer.objects.all()
            user = self.request.query_params.get('creator_id')
            min_price = self.request.query_params.get('min_price')
            max_delivery_time = self.request.query_params.get('max_delivery_time')
            search = self.request.query_params.get('search')
            ordering = self.request.query_params.get('ordering', '-updated_at')

            if user:
                queryset = queryset.filter(user=user)

            if min_price:
                min_price = float(min_price)
                queryset = queryset.filter(price__gte=min_price)

            if max_delivery_time:
                max_delivery_time = int(max_delivery_time)
                queryset = queryset.filter(delivery_time_in_days__lte=max_delivery_time)

            if search:
                queryset = queryset.filter(
                    Q(title__icontains=search) | Q(description__icontains=search)
                )

            valid_ordering_fields = ['updated_at', '-updated_at', 'price', '-price']
            if ordering in valid_ordering_fields:
                self.get_serializer_context()
                queryset = queryset.order_by(ordering)
            return queryset

        except NotFound:
            return Response({
                "message": "Offer nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)


    
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


