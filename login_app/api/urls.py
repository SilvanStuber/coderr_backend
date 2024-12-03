from django.urls import path
from .views import CostomLoginView

urlpatterns = [
  path('', CostomLoginView.as_view(), name='login'),
]