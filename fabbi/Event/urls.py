from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'event_app'
router = DefaultRouter()
router.register('Event', views.EventViewSet,'eventrouter')



urlpatterns = [
    path('', include(router.urls)),
]
