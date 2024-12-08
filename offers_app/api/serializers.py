from rest_framework import serializers
from offers_app.models import Offer, OfferDetail

class OfferDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDetail
        fields = ['id', 'title', 'revisions', 'delivery_time_in_days', 'price', 'features', 'offer_type']

class OfferSerializer(serializers.ModelSerializer):
    details = OfferDetailSerializer(many=True, required=True)
    user_details = serializers.SerializerMethodField()
    min_price = serializers.ReadOnlyField()
    min_delivery_time = serializers.ReadOnlyField()

    class Meta:
        model = Offer
        fields = ['id', 'user', 'title', 'image', 'description', 'created_at', 'updated_at', 
                  'details', 'min_price', 'min_delivery_time', 'user_details']

    def get_user_details(self, obj):
        user = obj.user
        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username
        }

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        if len(details_data) != 3 or not all(
            d['offer_type'] in ['basic', 'standard', 'premium'] for d in details_data
        ):
            raise serializers.ValidationError("Exactly 3 offer details with types 'basic', 'standard', and 'premium' are required.")

        offer = Offer.objects.create(**validated_data)
        for detail_data in details_data:
            OfferDetail.objects.create(offer=offer, **detail_data)

        return offer

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if details_data:
            for detail_data in details_data:
                detail = OfferDetail.objects.get(offer=instance, offer_type=detail_data['offer_type'])
                for attr, value in detail_data.items():
                    setattr(detail, attr, value)
                detail.save()

        instance.save()
        return instance
