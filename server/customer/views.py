from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer
from .renderers import ListCustomerRenderer

class ListCustomers(ListAPIView):
    renderer_classes = [ListCustomerRenderer]

    def get(self, request, format=None):
        # pylint: disable=E1101
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class CustomerDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        # pylint: disable=E1101
        return Customer.objects.filter(uuid=self.kwargs['uuid'])

class CreateCustomer(CreateAPIView):
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        return serializer.save()
