
from django.contrib import admin
from django.urls import path

#customize section
from.import views as v
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', v.index),
]
