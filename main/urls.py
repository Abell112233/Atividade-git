from django.contrib import admin
from django.urls import path
from Abell1.views import index, Abell1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index")
]
