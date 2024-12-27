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

    def to_representation(self, instance):
            queryset_called = self.context.get('queryset_called', False)
            data = super().to_representation(instance)
            if queryset_called == True:
                limited_data = generate_data_details_url(data)
            else: 
                limited_data = generate_data_details_all(data)
            return limited_data

    def create(self, validated_data):
        details_data = validated_data.pop('details', [])
        if len(details_data) != 3:
            raise serializers.ValidationError("An offer must have exactly three details (basic, standard, premium).") 
        offer = Offer.objects.create(**validated_data)  
        offer.min_price = min(item['price'] for item in details_data)
        offer.min_delivery_time = min(item['delivery_time_in_days'] for item in details_data)
        offer.user_details = generate_user_data(offer.user)
        generate_offer_detail(details_data, offer)
        print("%.2f" % offer.min_price)
        print(type("%.2f" % offer.min_price))
        offer.save()
        return offer
    
    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', [])
        instance.min_price = min(item['price'] for item in details_data)
        instance.min_delivery_time = min(item['delivery_time_in_days'] for item in details_data)
        if details_data:
            instance.details = []  
            for detail_data in details_data:
                detail_serializer = OfferDetailSerializer(data=detail_data)
                detail_serializer.is_valid(raise_exception=True)
                detail = detail_serializer.save()
                detail_url = str(f"/offerdetails/{detail.pk}/")
                instance.details.append({"id": detail.pk, "url": detail_url, "title": detail_data['title'], "revisions": detail_data['revisions'],  "delivery_time_in_days": detail_data['delivery_time_in_days'], "price": detail_data['price'],  "features": detail_data['features'],  "offer_type": detail_data['offer_type']}) 
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
            offer.details.append({"id": detail.pk, "url": detail_url, "title": detail_data['title'], "revisions": detail_data['revisions'],  "delivery_time_in_days": detail_data['delivery_time_in_days'], "price": detail_data['price'],  "features": detail_data['features'],  "offer_type": detail_data['offer_type']}) 

def generate_user_data(user_id): 
    profile = Profile.objects.get(id=user_id)
    return {
                'first_name': profile.first_name, 
                'last_name': profile.last_name,
                'username': profile.username,
            }

def generate_data_details_url(data):
     return{
            "id": data["id"],
            "user": data["user"],
            "title": data["title"],
            "image": data["image"],
            "description": data["description"],
            "created_at": data["created_at"],
            "updated_at": data["updated_at"],
            "details": [
                        {
                            "id": detail["id"],
                            "url": detail["url"],
                        }
                        for detail in data["details"]
                    ],
            "min_price": data["min_price"],
            "min_delivery_time": data["min_delivery_time"],
            "user_details": data["user_details"]
            }     

def generate_data_details_all(data):
     return{
            "id": data["id"],
            "user": data["user"],
            "title": data["title"],
            "image": data["image"],
            "description": data["description"],
            "created_at": data["created_at"],
            "updated_at": data["updated_at"],
            "details": [
                        {   
                            "id": detail["id"],
                            "title": detail["title"],
                            "revisions": detail["revisions"],
                            "delivery_time_in_days": detail["delivery_time_in_days"],
                            "price": detail["price"],
                            "features": detail["features"],
                            "offer_type": detail["offer_type"],
                        }
                        for detail in data["details"]
                    ],
            "min_price": data["min_price"],
            "min_delivery_time": data["min_delivery_time"],
            "user_details": data["user_details"]
            }