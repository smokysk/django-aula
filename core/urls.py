from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('state', viewsets.StateViewSet)
router.register('city', viewsets.CityViewSet)
router.register('zone', viewsets.ZoneViewSet)
router.register('district', viewsets.DistrictViewSet)

urlpatterns = router.urls
