from rest_framework import serializers
from offers_app.models import Offer, OfferDetail
from profile_app.models import Profile
from rest_framework import serializers

class OfferDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDetail
        fields = ['id', 'user', 'title', 'revisions', 'delivery_time_in_days', 'price', 'features', 'offer_type', 'user']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'user', 'title', 'image', 'description', 'created_at', 'updated_at', 'details', 'min_price', 'min_delivery_time', 'user_details']

    def create(self, validated_data):
        details_data = validated_data.pop('details', [])
        if len(details_data) != 3:
            raise serializers.ValidationError("An offer must have exactly three details (basic, standard, premium).") 
        offer = Offer.objects.create(**validated_data)  
        offer.min_price = min(item['price'] for item in details_data)
        offer.min_delivery_time = min(item['delivery_time_in_days'] for item in details_data)
        offer.user_details = generate_user_data(offer.user)
        generate_offer_detail(details_data, offer)
        offer.save()
        return offer
    
    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', [])
        if details_data:
            instance.details = []  
            for detail_data in details_data:
                detail_serializer = OfferDetailSerializer(data=detail_data)
                detail_serializer.is_valid(raise_exception=True)
                detail = detail_serializer.save()
                detail_url = str(f"/offerdetails/{detail.pk}/")
                instance.details.append({"id": detail.pk, "url": detail_url})
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

def generate_offer_detail(details_data, offer):
    for detail_data in details_data:
            detail_data['user'] = offer.user
            detail_serializer = OfferDetailSerializer(data=detail_data)
            detail_serializer.is_valid(raise_exception=True)
            detail = detail_serializer.save()
            detail_url = str(f"/offerdetails/{detail.pk}/")
            offer.details.append({"id": detail.pk, "url": detail_url}) 

def generate_user_data(user_id): 
    profile = Profile.objects.get(id=user_id)
    return {
                'first_name': profile.first_name, 
                'last_name': profile.last_name,
                'username': profile.username,
            }
       