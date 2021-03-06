from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('api/', include('SynerD.api.url', namespace='api')),
	path('', views.index, name = 'index'),
	path('Register/', views.register, name = 'Register'),
	path('Member/', views.member, name = 'Member'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

