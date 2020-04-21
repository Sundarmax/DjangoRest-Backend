from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('testapp.urls')),
    path('api/', include('testapp2.urls')),
    path('api/', include('testapp3.urls')),
    path('api/', include('testapp4.urls')),
    path('api/', include('testapp5.urls'))
]