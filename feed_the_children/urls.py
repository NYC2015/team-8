from feed_the_children import views

from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/', views.register, name='register'),
    url(r'login/', views.user_login, name='login'),
    url(r'logout/', views.user_logout, name='logout'),
    url(r'list/', views.list_of_food, name='list_of_food'),
    url(r'food/', views.get_food, name='get_food'),
]