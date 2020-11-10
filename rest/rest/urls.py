from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('testapp.urls')),
    path('api/', include('testapp2.urls')),
    path('api/', include('testapp3.urls')),
    path('api/', include('testapp4.urls')),
    path('api/', include('testapp5.urls')),
    path('api/', include('testapp6.urls')),
    path('api/', include('testapp7.urls')),
    path('api/', include('testapp8.urls')),
    path('api/', include('testapp9.urls')),
    path('api/', include('testapp10.urls')),
    path('api/', include('zoho_test.urls'))
]