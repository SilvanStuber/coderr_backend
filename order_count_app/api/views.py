from rest_framework import generics
from rest_framework.response import Response
from orders_app.models import Order
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import NotFound        

class OrderCountView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id):
        try:
            count = Order.objects.filter(business_user=business_user_id, status="in_progress").count()
            return Response(count, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "message": "Ordxer nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)
             

class CompletedOrderCountView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, business_user_id):
        try:
            count = Order.objects.filter(business_user=business_user_id, status="completed").count()
            return Response(count, status=status.HTTP_200_OK)
        except NotFound:
            return Response({
                "message": "Ordxer nicht gefunden"
            }, status=status.HTTP_404_NOT_FOUND)
