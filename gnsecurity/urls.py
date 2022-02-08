from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home" ),
    path('about/', views.about, name="about" ),
    path('gallery/', views.gallery, name="gallery" ),
    path('services/', views.services, name="services" ),
    path('contactus/', views.contactus, name="contactus" )
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
