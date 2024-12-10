from django.db import models
from django.db import models

class Offer(models.Model):
    user = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class OfferDetail(models.Model):
    OFFER_TYPES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]

    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="details")
    title = models.CharField(max_length=255)
    revisions = models.IntegerField()
    delivery_time_in_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField()
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPES)

    def __str__(self):
        return f"{self.title} ({self.offer_type})"

