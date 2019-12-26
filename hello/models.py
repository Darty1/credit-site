from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Named(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Product(Named):
    interest_rate = models.FloatField(null=True, blank=True)
    min_date = models.FloatField()
    max_date = models.IntegerField()
    sum = models.IntegerField()
    early_repayment = models.BooleanField(verbose_name='early repayment', default=False)


class Consumer(models.Model):
    class Meta:
        verbose_name = 'consumer'
        verbose_name_plural = 'consumers'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wish_list = models.ManyToManyField(Product)
