from django.contrib import admin
from django.urls import path, include
from App import views
from Candidates import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # frontend
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login/', include('django.contrib.auth.urls')),
    # backend 
    path('candidate', views.backend, name='backend'),
    path('candidate/<int:id>/', views.candidate, name='candidate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
