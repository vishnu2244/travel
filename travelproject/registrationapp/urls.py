from . import views
from django.urls import path,include

urlpatterns = [

    path('userform', views.userform,name='userform'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),

]