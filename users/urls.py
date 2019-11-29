from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name="users")
router.register(r'groups', views.GroupViewSet, base_name="groups")

app_name = "rest"
urlpatterns = [
    path('', include(router.urls)),
]
