from django.contrib import admin
from django.urls import path, include
from practiceapp import urls as app_urls
from practiceapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('app/', include(app_urls)),
]
