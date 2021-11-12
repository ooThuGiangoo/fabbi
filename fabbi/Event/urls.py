from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'event_app'
router = DefaultRouter()
router.register('event', views.EventViewSet,'eventrouter')



urlpatterns = [
    path('', include(router.urls)),
    path('eventt', views.EventAPIView.as_view()),
    path('eventt/<int:pk>', views.DetailEvent.as_view())
]
