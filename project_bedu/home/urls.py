from django.urls import path, include
from .views import HomeView,PostView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('<int:pk>/',PostView.as_view(),name='post'),
    path('',HomeView.as_view())
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
