from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.authtoken.views import ObtainAuthToken

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
