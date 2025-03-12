
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#link other apps urls.py files with the main path

urlpatterns = [
path('', include('home.urls')),
path('admin/', admin.site.urls),
path('about/',include('about.urls')),
path('accounts/', include('accounts.urls')),
path('publishing/', include('publishing.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
