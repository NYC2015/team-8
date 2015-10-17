from donor import views

from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/', views.register, name='register'),
    url(r'login/', views.donor_login, name='login'),
    url(r'logout/', views.donor_logout, name='logout'),
    url(r'picupload/', views.upload_picture, name='pic_upload'),
]