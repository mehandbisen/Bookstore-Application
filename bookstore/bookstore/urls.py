from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

from django.contrib import admin
from django.urls import path, include  # ✅ include is required to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # ✅ this includes your app's URL patterns
]
