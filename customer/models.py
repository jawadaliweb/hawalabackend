from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    phone = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    receive = models.IntegerField(default=0)
    payment = models.IntegerField(default=0)

    def __str__(self):
        return self.name
 