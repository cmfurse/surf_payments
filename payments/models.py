from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True)
    player_name = models.CharField(max_length=50, null=True)
    balance = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.email


class Fee(models.Model):
    description = models.CharField(max_length=255)
    recurring = models.BooleanField(default=False)
    recurring_day_of_month = models.PositiveSmallIntegerField(default=0)
    due_date = models.DateField(null=True)
    amount = models.PositiveSmallIntegerField(default=0)
    split_per_player = models.BooleanField(default=False)

    def __str__(self):
        return  f'{self.description} - ${self.amount}'


class PaymentRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    due_date = models.DateField()
    amount = models.PositiveSmallIntegerField(default=0)
    paid = models.BooleanField(default=False)
