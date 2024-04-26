from rest_framework import routers
from jambo.apps.customers import views

router = routers.SimpleRouter(trailing_slash=False)
router.register('business-categories', views.BusinessCategoryViewSet)
router.register('business-locations', views.BusinessLocationViewSet)
router.register('businesses', views.BusinessViewSet)
router.register('customer-contacts', views.CustomerContactViewSet)
router.register('customers', views.CustomerViewSet)

urlpatterns = router.urls
