from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from orders_app.models import Order
from offers_app.models import OfferDetail
from .serializers import OrderSerializer, CreateOrderSerializer

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(customer_user=user) | Order.objects.filter(business_user=user)

class OrderCreateView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        order = self.get_object()
        if "status" in request.data:
            order.status = request.data["status"]
            order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)

class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAdminUser]

class OrderCountView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, business_user_id):
        count = Order.objects.filter(business_user_id=business_user_id, status="in_progress").count()
        return Response({"order_count": count})

class CompletedOrderCountView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, business_user_id):
        count = Order.objects.filter(business_user_id=business_user_id, status="completed").count()
        return Response({"completed_order_count": count})
