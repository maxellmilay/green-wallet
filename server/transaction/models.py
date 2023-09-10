from django.db import models
import uuid
from social_auth.models import GoogleUser

class TransactionGroup(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(GoogleUser, editable=False, on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Transaction(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    group = models.ForeignKey(TransactionGroup, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

