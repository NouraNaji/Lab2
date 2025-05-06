from django.contrib import admin
from django.urls import include, path
from apps.bookmodule import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('books/', include("apps.bookmodule.urls")),  
    path('users/', include("apps.usermodule.urls")),  
    
    path('users/', include('users.urls')),  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)