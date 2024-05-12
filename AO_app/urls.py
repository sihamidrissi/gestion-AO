
from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
]
