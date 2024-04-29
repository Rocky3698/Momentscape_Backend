from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('posts', views.PostViewset)
router.register('comment', views.CommentViewset)
router.register('react', views.ReactViewset)
urlpatterns = [
    path('', include(router.urls)),
]
