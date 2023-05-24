
from django.contrib import admin
from django.urls import path

#customize section
from.import views as v
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', v.index),#localhost:port no/root dir
    path('store/', v.store, name='store'),
]
