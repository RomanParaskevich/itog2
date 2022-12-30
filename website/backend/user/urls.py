from rest_framework import routers
from .views import UserViewSet

user_router = routers.DefaultRouter()
user_router.register('', UserViewSet)

urlpatterns = []
urlpatterns += user_router.urls
