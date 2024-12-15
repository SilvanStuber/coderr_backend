from django.urls import path
from .views import (OrderCountView, CompletedOrderCountView)

urlpatterns = [
    path('<int:business_user_id>/', OrderCountView.as_view(), name='order-count'),
    path('<int:business_user_id>/', CompletedOrderCountView.as_view(), name='completed-order-count'),
]
