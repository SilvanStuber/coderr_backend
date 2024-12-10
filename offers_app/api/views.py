from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from offers_app.models import Offer, OfferDetail
from .serializers import OfferSerializer, OfferDetailSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView


class OfferListView(generics.ListCreateAPIView):
    queryset = Offer.objects.all().order_by('-updated_at')
    serializer_class = OfferDetailSerializer
    permission_classes = [IsAuthenticated]

class OfferListView(ListAPIView):
    serializer_class = OfferDetailSerializer

    def get_queryset(self):
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
            queryset = queryset.order_by(ordering)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {"message": "No offers found."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
