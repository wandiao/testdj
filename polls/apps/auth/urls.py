# coding=utf-8

from django.conf.urls import url

from rest_framework_jwt import views as jwt_views
from . import views

urlpatterns = [
  url(
    r'^token/profile/get/',
    views.JWTPCLoginView.as_view(),
  ),
]