import os

from django.shortcuts import redirect

from rest_framework.views import APIView

from .services import create_jwt_token
from .serializers import InputSerializer

class GoogleSocialAuthView(APIView):
    def get(self, request):
        input_serializer = InputSerializer(data=request.GET)
        input_serializer.is_valid(raise_exception=True)

        validated_data = input_serializer.validated_data
        user_data, jwt_token = create_jwt_token(validated_data)

        response = redirect(f"{os.environ.get('BASE_FRONTEND_URL')}/dashboard")
        response.set_cookie('Token',jwt_token, max_age = 60 * 24 * 60 * 60)

        return response
