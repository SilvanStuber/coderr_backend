from django.db import models
class Review(models.Model):
    business_user = models.IntegerField()
    reviewer = models.IntegerField()
    rating = models.PositiveSmallIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('business_user', 'reviewer')
