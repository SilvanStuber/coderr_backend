from django.urls import path
from .views import (
    OrderListView, OrderCountView, CompletedOrderCountView
)

order_patterns = [
    path('', OrderListView.as_view({'get': 'list', 'post': 'create', 'patch': 'partial_update', 'delete': 'destroy'}), name='order-list'),
    path('<int:pk>/', OrderListView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='order-detail'),
]


order_count_patterns = [
    path('<int:business_user_id>/', OrderCountView.as_view({'get': 'retrieve'}), name='order-count'),
    path('<int:business_user_id>/completed/', CompletedOrderCountView.as_view({'get': 'retrieve'}), name='completed-order-count'),
]


