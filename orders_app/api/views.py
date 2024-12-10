from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from orders_app.models import Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer, CreateOrderSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            user = self.request.user
            orders = Order.objects.filter(customer_user=user) | Order.objects.filter(business_user=user)
            serializer = self.get_serializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "ok": False,
                "status": 404,
                "message": "Order nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)


        

class OrderCreateView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        order = self.get_object()
        if "status" in request.data:
            order.status = request.data["status"]
            order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)

class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

class OrderCountView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id):
        count = Order.objects.filter(business_user_id=business_user_id, status="in_progress").count()
        return Response({"order_count": count})

class CompletedOrderCountView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id):
        count = Order.objects.filter(business_user_id=business_user_id, status="completed").count()
        return Response({"completed_order_count": count})
