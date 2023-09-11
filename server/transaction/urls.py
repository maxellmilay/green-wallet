from django.urls import path

from .views import ListTransactions, TransactionDetail, CreateTransaction, CreateGroup, TransactionGroupDetail, ListGroups

urlpatterns = [
    path('list/<str:group>',ListTransactions.as_view(), name='List Transactions from Group'),
    path('<uuid:uuid>',TransactionDetail.as_view(), name='Retrieve Transaction'),
    path('create-transaction',CreateTransaction.as_view(), name='Create Transaction'),
    path('group', ListGroups.as_view(), name="List Transaction Groups"),
    path('group/<uuid:uuid>', TransactionGroupDetail.as_view(), name='Retrieve Transaction Group'),
    path('create-group', CreateGroup.as_view(), name='Create Transaction Group')
]

