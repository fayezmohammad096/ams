
from django.urls import path

#customize section
from.import views as v
urlpatterns = [
    
    path('brand/', v.index,name='brand'),#localhost:port no/root dir

]
    
    