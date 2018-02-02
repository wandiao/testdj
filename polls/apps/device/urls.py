from django.conf.urls import url
from rest_framework import routers

import views

router = routers.DefaultRouter()
router.register(r'device/api', views.DeviceViewSet)

urlpatterns = router.urls

urlpatterns += [
  url(r'^test$', views.testView),
]