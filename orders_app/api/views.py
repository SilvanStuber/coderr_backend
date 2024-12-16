from rest_framework import generics
from rest_framework.response import Response
from rest_framework import  viewsets
from orders_app.models import Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer, CreateOrderSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound

class OrderListView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            user = self.request.user
            orders = Order.objects.filter(customer_user=user) | Order.objects.filter(business_user=user)
            serializer = self.get_serializer(orders)
            return serializer.data
        except NotFound:
            return Response({
                "message": "Order nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        # Verwende den CreateOrderSerializer
        serializer = CreateOrderSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        # Speichere die Order
        order = serializer.save()
        
        # Erstelle die Antwort
        response_serializer = self.get_serializer(order)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance):
        instance.delete()


class OrderCountView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id):
        try:
            count = Order.objects.filter(business_user=business_user_id, status="in_progress").count()
            return count
        except NotFound:
            return Response({
                "message": "Order nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)
             

class CompletedOrderCountView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id):
        try:
            count = Order.objects.filter(business_user=business_user_id, status="completed").count()
            return count
        except NotFound:
            return Response({
                "message": "Order nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)