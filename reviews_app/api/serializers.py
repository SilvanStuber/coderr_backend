from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from reviews_app.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'business_user', 'reviewer', 'rating', 'description', 'created_at', 'updated_at']
        read_only_fields = ['business_user', 'reviewer']

    def validate(self, request_data):
        print("request_data",request_data)
        business_user = self.context['request'].data.get('business_user')
        if self.context['request'].method == 'POST':
            if Review.objects.filter(business_user=business_user, reviewer=self.context['request'].user).exists():
                raise ValidationError("You can only leave one review per business user.")
        return request_data

    def update(self, instance, validated_data):
        validated_data.pop('business_user', None)
        validated_data.pop('reviewer', None)
        return super().update(instance, validated_data)
