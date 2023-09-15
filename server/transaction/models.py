from django.db import models
import uuid
from json import JSONEncoder
from social_auth.models import GoogleUser

# UUID not serializable fix
JSONEncoder_olddefault = JSONEncoder.default
def JSONEncoder_newdefault(self, o):
    if isinstance(o, uuid.UUID): return str(o)
    return JSONEncoder_olddefault(self, o)
JSONEncoder.default = JSONEncoder_newdefault

class TransactionGroup(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(GoogleUser, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    expenses = models.IntegerField(default=0)
    income = models.IntegerField(default=0)
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

