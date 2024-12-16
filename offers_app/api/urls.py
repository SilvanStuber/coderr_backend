from django.urls import path
from .views import OfferViewSet, OfferDetailViewSet


offer_patterns = [
    path('', OfferViewSet.as_view({'get': 'list', 'post': 'create'}), name='offer-list'),
    path('<int:pk>/', OfferViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='offer-detail'),
]

offerdetail_patterns = [
    path('<int:pk>/', OfferDetailViewSet.as_view({'get': 'retrieve'}), name='offer-detail-specific'),
]
