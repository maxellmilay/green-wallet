from sileo.resource import Resource
from sileo.registration import register

from transaction.models import Transaction
from transaction.forms import TransactionForm

class TransactionResource(Resource):
    query_set = Transaction.objects.all()
    fields = ['uuid','name','amount']
    allowed_methods = ['get_pk','filter','create','update','delete']
    update_filter_fields = ['uuid']
    delete_filter_fields = ['uuid']
    filter_fields = ['uuid']
    form_class = TransactionForm

register('transaction','transaction',TransactionResource,version='v1')

        
