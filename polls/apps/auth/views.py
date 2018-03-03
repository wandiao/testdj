# coding: utf-8

import datetime

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken

from rest_framework.response import Response

from polls.common import (
    serializers as common_serializers,
)
from . import serializers

class JWTLoginView(ObtainJSONWebToken):
  serializer_class = None

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    if serializer.is_valid():
      user = serializer.object.get('user') or request.user
      user.last_login = datetime.datetime.now()
      user.save()
      token = serializer.object.get('token')
      response_data = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER(token, user, request)
      profile_serializer = common_serializers.ProfileDetailSerializer(instance=user.profile)
      response_data.update({
        'expires_in': api_settings.JWT_EXPIRATION_DELTA,
        'profile': profile_serializer.data
      })
      return Response(response_data)
    return Response(serializer.errors, status=400)

class JWTPCLoginView(JWTLoginView):
  '''
    电脑浏览器端登录接口
    ---
    POST:
      parameters:
        - name: username
          description: 用户名
          type: string
        - name: password
          description: 密码
          type: string
      omit_serializer: true
  '''
  serializer_class = serializers.PCLoginSerializer


