from rest_framework import serializers
from .models import GoogleUser

class InputSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    error = serializers.CharField(required=False)

class GoogleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleUser
        fields = ['uuid','first_name','last_name','email','picture','balance','expenses','income','created']
