from django.urls import path
from rest_framework import routers
from .views.users import UserViewSet
from .views.periods import PeriodView, PeriodsView
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('periods/', PeriodsView.as_view(), name='index'),
    path('periods/<int:pk>', PeriodView.as_view(), name='period'),
]