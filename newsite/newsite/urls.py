from django.contrib import admin
from django.urls import path
from company.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('company.urls')),

]
