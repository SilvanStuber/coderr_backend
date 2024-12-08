from django.urls import path
from .views import OfferListView, OfferDetailView, OfferDetailSpecificView

urlpatterns = [
    path('', OfferListView.as_view(), name='offer-list'),
    path('<int:pk>/', OfferDetailView.as_view(), name='offer-detail'),
    path('offerdetails/<int:pk>/', OfferDetailSpecificView.as_view(), name='offer-detail-specific'),
]
