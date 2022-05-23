from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'co', views.COTObjectViewSet)
router.register(r'tf', views.CPTransformViewSet)

urlpatterns = [
    path('', include(router.urls)),
#    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]