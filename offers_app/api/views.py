from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from offers_app.models import Offer, OfferDetail
from .serializers import OfferSerializer, OfferDetailSerializer

class OfferListView(generics.ListCreateAPIView):
    queryset = Offer.objects.all().order_by('-updated_at')
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.query_params.get('creator_id')
        min_price = self.request.query_params.get('min_price')
        max_delivery_time = self.request.query_params.get('max_delivery_time')
        search = self.request.query_params.get('search')
        ordering = self.request.query_params.get('ordering', '-updated_at')

        if user:
            queryset = queryset.filter(user__id=user)

        if min_price:
            queryset = queryset.filter(details__price__gte=min_price)

        if max_delivery_time:
            queryset = queryset.filter(details__delivery_time_in_days__lte=max_delivery_time)
  
        if search:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(description__icontains=search)

        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OfferDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE', 'PATCH']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

class OfferDetailSpecificView(generics.RetrieveAPIView):
    queryset = OfferDetail.objects.all()
    serializer_class = OfferDetailSerializer
    permission_classes = [IsAuthenticated]
