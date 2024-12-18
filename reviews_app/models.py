from django.db import models
from django.contrib.auth.models import User

# models.py
class Review(models.Model):
    business_user = models.CharField(max_length=100, default="")
    reviewer = models.CharField(max_length=100, default="")
    rating = models.PositiveSmallIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('business_user', 'reviewer')
