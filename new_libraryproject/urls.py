from django.contrib import admin
from django.urls import path, include
from apps.bookmodule import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/", include("apps.bookmodule.urls")),  # تأكد أن include يشير إلى الملف الصحيح
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)