from django.contrib import admin
from donor import models

# Register your models here.
admin.site.register(models.DonorProfile)
admin.site.register(models.Store)
admin.site.register(models.Food)
admin.site.register(models.Coupon)
