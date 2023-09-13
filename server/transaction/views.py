from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView, CreateAPIView

from django.db.models import Q, Sum

from .models import Transaction, TransactionGroup
from .serializers import TransactionSerializer, TransactionGroupSerializer
from social_auth.models import GoogleUser

class ListTransactions(ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        uuid = self.kwargs['uuid']
        #pylint: disable=E1101
        transactions = Transaction.objects.filter(group__uuid=uuid)
        return sorted(transactions,key=lambda x: x.created)
    
class ListGroups(ListAPIView):
    serializer_class = TransactionGroupSerializer

    def get_queryset(self):
        uuid = self.kwargs['uuid']
        #pylint: disable=E1101
        groups = TransactionGroup.objects.filter(owner__uuid=uuid)
        for group in groups:
            transactions = Transaction.objects.filter(group=group.uuid)     

            group.income = transactions.aggregate(value=Sum('amount',filter=Q(amount__gt=0))).get('value')
            group.expenses = transactions.aggregate(value=Sum('amount',filter=Q(amount__lt=0))).get('value')
            
            if group.income is None:
                group.income = 0
                if group.expenses is None:
                    group.expenses = 0
                    group.balance = 0
                else:
                    group.balance = group.expenses
            else:
                if group.expenses is None:
                    group.expenses = 0
                    group.balance = group.income
                else:
                    group.balance = transactions.aggregate(value=Sum('amount')).get('value')

            group.save()
        return groups

class TransactionDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    lookup_field = 'uuid'
    
    def get_queryset(self):
        uuid = self.kwargs['uuid']
        #pylint: disable=E1101
        transaction = Transaction.objects.filter(uuid=uuid)
        return transaction

class TransactionGroupDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionGroupSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        uuid = self.kwargs['uuid']
        #pylint: disable=E1101
        group = TransactionGroup.objects.filter(uuid=uuid)
        return group
    
class CreateTransaction(CreateAPIView):
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        return serializer.save()

class CreateGroup(CreateAPIView):
    serializer_class = TransactionGroupSerializer

    def perform_create(self, serializer):
        return serializer.save()
