
from django.urls import path

#customize section
from.import views as v
urlpatterns = [
    
    path('register/', v.index,name='register_form'),#localhost:port no/root dir
    path('verification/<v_key>', v.verify),
    path('store/', v.store, name='store'),
    path("login/",v.login),
    path("login_auth/",v.login_auth, name='login_auth'),
]
    
    