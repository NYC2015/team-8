from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50, help_text='Store name', default='No name provided')
    address = models.CharField(max_length=50, help_text='Address', default='No address provided')
    state = models.CharField(max_length=2, help_text='State', default='No state provided')
    zip = models.IntegerField(help_text='Zip code', default='000000')

    def __unicode__(self):
        return self.name


class DonorProfile(models.Model):
    user = models.OneToOneField(User)
    store = models.ForeignKey(Store, default=None)

    def __unicode__(self):
        return str(self.user)


class Food(models.Model):
    store = models.ForeignKey(Store)
    name = models.CharField(max_length=50, help_text='Name of the food', default='No name provided')
    quantity = models.IntegerField(help_text='Quantity for donation', default='2')
    weight = models.IntegerField(help_text='Weight of the food', default='1')
    category = models.CharField(max_length=50, help_text='Category of food', default='No category provided')

    def __unicode__(self):
        return self.name


class Coupon(models.Model):
    food = models.ForeignKey(Food)
    code = models.IntegerField(help_text='Coupon code', default=0)
    quantity = models.IntegerField(help_text='Quantity of coupons')

    def __unicode__(self):
        return self.code
