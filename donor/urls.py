from donor import views

from django.conf.urls import url

urlpatterns = [
    url(r'register/', views.register, name='register'),
    url(r'login/', views.donor_login, name='login'),
    url(r'logout/', views.donor_logout, name='logout'),
    url(r'sale/',views.sale, name='sale'),
]
