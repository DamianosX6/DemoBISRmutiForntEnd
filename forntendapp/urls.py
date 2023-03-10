from nturl2path import url2pathname
from django.urls import path , re_path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'forntendapp'

urlpatterns = [
 
  path('register',views.register,name='register'),
  path('logout',views.logoutuser,name='logout'),
  path('login',views.loginPage,name='login'),

  path('',views.index,name='index'),





]
from django.conf import settings  
from django.conf.urls.static import static  
  
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  