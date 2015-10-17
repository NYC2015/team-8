from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=50, help_text='Address', default='No address provided')
    state = models.CharField(max_length=2, help_text='State', default='No state provided')
    zip = models.IntegerField(help_text='Zip code', default='000000')
    net_income = models.IntegerField(help_text='Income per month', default='000000')
    household_size = models.IntegerField(help_text='Household size', default='1')

    def __unicode__(self):
        return str(self.user)
