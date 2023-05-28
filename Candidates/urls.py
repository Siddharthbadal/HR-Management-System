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
    path('candidates', views.backend, name='backend'),
    path('candidates/<int:id>/', views.candidate, name='candidate'),
    path('<int:id>/download_candidate_pdf/', views.download_candidate_pdf, name='download_candidate_pdf')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
