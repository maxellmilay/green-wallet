from django.urls import path
from .views import ListCustomers, CustomerDetail,CreateCustomer

urlpatterns = [
    path('',ListCustomers.as_view(), name='list-customers'),
    path('<uuid:uuid>', CustomerDetail.as_view(),name='get-update-delete-single-customer'),
    path('create', CreateCustomer.as_view(), name='create-customer')
]

