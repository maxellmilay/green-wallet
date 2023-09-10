from django.db import models
import uuid

class GoogleUser(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    picture = models.URLField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
