from rest_framework import serializers

from djoser.serializers import UserSerializer

from .models import Customer
from accounts.models import *

class CustomerSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField(read_only=True)
    receive = serializers.IntegerField(read_only=True)
    payment = serializers.IntegerField(read_only=True)
    class Meta:
        model = Customer
        fields = ['id','name','address','phone','amount','receive','payment']
        


class MyUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'first_name']