from rest_framework.routers import DefaultRouter
from django.urls import include, path
from post import views

# 라우터가 없다면?

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]

