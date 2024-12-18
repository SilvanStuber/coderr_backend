from django.urls import path
from .views import (
    OrderListView, OrderCountView, CompletedOrderCountView
)

order_patterns = [
    path('', OrderListView.as_view({'get': 'list', 'post': 'create', 'patch': 'partial_update', 'delete': 'destroy'}), name='order-list'),
    path('<int:pk>/', OrderListView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='order-detail'),
]

order_count_patterns = [
    path('<int:business_user_id>/', OrderCountView.as_view(), name='order-count'),
]

completed_order_count_patterns = [
    path('<int:business_user_id>/', CompletedOrderCountView.as_view(), name='completed-order-count'),
]


