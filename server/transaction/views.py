from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Transaction, TransactionGroup
from .serializers import TransactionSerializer, TransactionGroupSerializer

class ListTransactions(ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        group = self.kwargs['group']
        #pylint: disable=E1101
        transactions = Transaction.objects.filter(group__name=group)
        return transactions

class TransactionDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    lookup_field = 'uuid'
    
    def get_queryset(self):
        uuid = self.kwargs['uuid']
        #pylint: disable=E1101
        transaction = Transaction.objects.filter(uuid=uuid)
        return transaction

class CreateTransaction(CreateAPIView):
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        return serializer.save()

class TransactionGroupDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionGroupSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        uuid = self.kwargs['uuid']
        #pylint: disable=E1101
        group = TransactionGroup.objects.filter(uuid=uuid)
        return group
