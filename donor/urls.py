from donor import views

from django.conf.urls import url

urlpatterns = [
    url(r'^sale',views.sale, name='sale'),
]
