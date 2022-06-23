from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from questions.admin import teacher_site, student_site

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('teacher-admin/', teacher_site.urls),
    path('student-admin/', student_site.urls),
    path('', include('main.urls')),
    path('auth/', include('accounts.urls')),
    path('quest/', include('questions.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
