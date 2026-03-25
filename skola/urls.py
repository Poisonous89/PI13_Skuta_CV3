from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ZMENA JE TU:
    path('kruzky/', include('kruzky.urls')), 
]