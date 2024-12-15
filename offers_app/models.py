from django.db import models
from django.db import models

class OfferDetail(models.Model):
    OFFER_TYPES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium')
    ]

    title = models.CharField(max_length=255)
    revisions = models.IntegerField(null=True, blank=True)
    delivery_time_in_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField()
    offer_type = models.CharField(max_length=20, choices=OFFER_TYPES)

class Offer(models.Model):
    user = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=255)
    image =  models.ImageField(upload_to='profile_pictures/', null=True, )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    details = models.JSONField(default=list) 
    min_price = models.CharField(max_length=255, blank=True)
    min_delivery_time = models.CharField(max_length=255, blank=True)
    user_details = models.JSONField(default=list, blank=True) 
