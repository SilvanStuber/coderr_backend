from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Offer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="offers"
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="offers/images/", null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def min_price(self):
        return self.details.aggregate(models.Min('price'))['price__min']

    @property
    def min_delivery_time(self):
        return self.details.aggregate(models.Min('delivery_time_in_days'))['delivery_time_in_days__min']


class OfferDetail(models.Model):
    OFFER_TYPES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]

    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, related_name="details"
    )
    title = models.CharField(max_length=255)
    revisions = models.IntegerField(default=0)
    delivery_time_in_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField()
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPES)

    class Meta:
        unique_together = ('offer', 'offer_type')

    def __str__(self):
        return f"{self.offer.title} - {self.offer_type.capitalize()}"

