from django.db import models
from rest_framework import serializers


ACCOUNT_TYPES =(
    (1, "Cash in Hand"),
    (2, "Bank Account"),
)

VOUCHER_TYPES = (
    (1, "Payment"),
    (2, "Receive"),
)

class Account(models.Model):
    name = models.CharField(max_length=50)
    type = models.IntegerField(choices=ACCOUNT_TYPES)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return self.name + " - " + self.get_type_display()



class Transaction(models.Model):
    amount = models.IntegerField()
    account = models.ForeignKey("Account",  on_delete=models.CASCADE)
    customer = models.ForeignKey("customer.Customer",  on_delete=models.CASCADE)
    voucher_type = models.IntegerField(choices=VOUCHER_TYPES)
    r_customer = models.ForeignKey("customer.Customer", related_name="receives", on_delete=models.CASCADE, null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.voucher_type == 1:
            self.customer.payment += self.amount
            self.customer.amount += self.amount
            self.account.amount += self.amount
        elif self.voucher_type == 2:
            self.customer.receive += self.amount
            self.r_customer.amount -= self.amount
            self.account.amount -= self.amount
            if self.r_customer.amount < 0 and self.amount:
                raise serializers.ValidationError([
                    {"customer amount": "Amount is going to minus"}
                ])
            self.r_customer.save()
        self.customer.save()
        self.account.save()
        super().save()

    def __str__(self):
        return  str(self.amount) + " - " + self.get_voucher_type_display() + " - " +  str(self.account)

