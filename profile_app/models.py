from django.db import models

class Profile(models.Model):
    user = models.IntegerField()
    username = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    file = models.ImageField(upload_to='profile_pictures/', default="")
    location = models.CharField(max_length=255, blank=True)
    tel = models.CharField(max_length=20, default="")
    description = models.TextField(blank=True)
    working_hours = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self