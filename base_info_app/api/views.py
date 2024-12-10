from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg
from profile_app.models import Profile
from offers_app.models import Offer
from .serializers import BaseInfoSerializer
from reviews_app.models import Review
from rest_framework.permissions import AllowAny

class BaseInfoView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        review_count = Review.objects.count()
        average_rating = Review.objects.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0.0
        business_profile_count = Profile.objects.filter(type='business').count()
        offer_count = Offer.objects.count()

        data = {
            "review_count": review_count,
            "average_rating": round(average_rating, 1),
            "business_profile_count": business_profile_count,
            "offer_count": offer_count,
        }

        serializer = BaseInfoSerializer(data)
        return Response(serializer.data)