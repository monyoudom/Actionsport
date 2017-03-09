from django.conf.urls import  url
from .  import views



urlpatterns = [

 url(r'^index/', views.index,name='index'),
 url(r'^resgister/', views.resigster, name='resigster'),
 url(r'^$',views.login,name='login'),
 url(r'^playground/',views.playground,name='playground'),
 url(r'^logout/',views.logouts,name = 'logouts')
  
    
  ]
