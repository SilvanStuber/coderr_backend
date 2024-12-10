from rest_framework import serializers


class BaseInfoSerializer(serializers.Serializer):
    review_count = serializers.IntegerField()
    average_rating = serializers.DecimalField(max_digits=2, decimal_places=1)
    business_profile_count = serializers.IntegerField()
    offer_count = serializers.IntegerField()