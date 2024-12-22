from django.urls import path
from .views import ProfileViewSets, ProfileCustomerViewSets, ProfileBusinessViewSets

urlpatterns = [
    path('<int:pk>/', ProfileViewSets.as_view(), name='profile-detail'),
    path('customer/', ProfileCustomerViewSets.as_view(), name='customer-list'),
    path('business/', ProfileBusinessViewSets.as_view(), name='business-list'),
]
