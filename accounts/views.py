from accounts.models import *
from .serializers import *
from rest_framework import viewsets
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AccountSerializer
        return AccountSerializer  


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransactionSerializer
        return TransactionSerializer  

