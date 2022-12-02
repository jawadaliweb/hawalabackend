from customer.models import Customer
from .serializers import CustomerSerializer
from rest_framework import viewsets
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from .serializers import *
from accounts.models import *
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    