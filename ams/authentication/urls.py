
from django.urls import path

#customize section
from.import views as v
urlpatterns = [
    
    path('', v.index),#localhost:port no/root dir
    path('store/', v.store, name='store'),
    path('verification/<v_key>', v.verify),
]
