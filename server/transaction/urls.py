from django.urls import path

from .views import ListTransactions, TransactionDetail, CreateTransaction, TransactionGroupDetail

urlpatterns = [
    path('list/<str:group>',ListTransactions.as_view(), name='List Transactions from Group'),
    path('<uuid:uuid>',TransactionDetail.as_view(), name='Retrieve Transaction'),
    path('create',CreateTransaction.as_view(), name='Create Transaction'),
    path('group/<uuid:uuid>', TransactionGroupDetail.as_view(), name='Retrieve Transaction Group')
]

