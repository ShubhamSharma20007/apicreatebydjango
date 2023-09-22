
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import Companyviewset

router = routers.DefaultRouter()
router.register(r'users', Companyviewset)


urlpatterns = [
    path('',include(router.urls))
]