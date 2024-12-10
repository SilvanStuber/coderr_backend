from django.db import models
from rest_framework import permissions, generics, filters
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from .permissions import IsCustomerProfile, IsReviewerOrAdmin
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ReviewSerializer
from reviews_app.models import Review

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['business_user', 'reviewer']
    ordering_fields = ['updated_at', 'rating']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), IsCustomerProfile()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewerOrAdmin]

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsReviewerOrAdmin()]
        return [permissions.AllowAny()]

    def partial_update(self, request, *args, **kwargs):
        self.kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)

