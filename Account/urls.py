from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('address', views.AddressViewset)
router.register('profile', views.ProfileViewset)
urlpatterns = [
    path('', include(router.urls)),
]
