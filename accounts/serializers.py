from rest_framework import serializers
from .models import *
from customer.serializers import CustomerSerializer

class AccountSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField(read_only=True)
    class Meta:
        model = Account
        fields = ['id','name','type','amount']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id','amount','account','customer','voucher_type','r_customer', 'created', 'updated']
