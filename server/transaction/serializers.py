from rest_framework import serializers
from .models import TransactionGroup,Transaction

class TransactionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionGroup
        fields = ['uuid', 'name', 'owner','created']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['uuid','name','group','amount','created']
