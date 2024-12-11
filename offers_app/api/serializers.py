from rest_framework import serializers
from offers_app.models import Offer, OfferDetail

class OfferDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferDetail
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    details = OfferDetailSerializer(many=True)
    
    class Meta:
        model = Offer
        fields = '__all__'

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        if len(details_data) != 3:
            raise serializers.ValidationError("An offer must have exactly three details (basic, standard, premium).")
        offer = Offer.objects.create(**validated_data)
        for detail_data in details_data:
            OfferDetail.objects.create(**detail_data, offer=offer)
        return offer
    
    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', None)
        if details_data:
            instance.details.clear()
            for detail_data in details_data:
                detail = OfferDetail.objects.create(**detail_data)
                instance.details.add(detail)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    
