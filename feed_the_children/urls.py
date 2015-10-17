from feed_the_children import views

from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/', views.register, name='register'),
    url(r'login/', views.user_login, name='login'),
]
