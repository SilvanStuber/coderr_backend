from django.urls import path
from .views import (
    OrderListView, OrderCreateView, OrderDetailView, 
    OrderUpdateView, OrderDeleteView, OrderCountView, CompletedOrderCountView
)

order_patterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
]

order_count_patterns = [
    path('<int:business_user_id>/', OrderCountView.as_view(), name='order-count'),
    path('<int:business_user_id>/completed/', CompletedOrderCountView.as_view(), name='completed-order-count'),
]


