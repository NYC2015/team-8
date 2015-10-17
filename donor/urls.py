from donor import views

from django.conf.urls import url

urlpatterns = [
    url(r'register/', views.register, name='register'),
    url(r'login/', views.donor_login, name='login'),
]