from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PasswordModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_url = models.URLField(max_length=200)
    username = models.CharField(max_length=250)
    site_password = models.CharField(max_length = 50)
    key = models.CharField(max_length=250)

    def __str__(self):
        return self.site_url
    