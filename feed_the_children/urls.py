from feed_the_children import views

from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
