from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name="expense_group")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name