from urllib.parse import urlencode
import os
import requests

from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from django.urls import reverse
from django.shortcuts import redirect

from .services import google_get_access_token, google_get_user_info

class GoogleSocialAuthView(APIView):
    class InputSerializer(serializers.Serializer):
        code = serializers.CharField(required=False)
        error = serializers.CharField(required=False)

    def get(self, request):
        input_serializer = self.InputSerializer(data=request.GET)
        input_serializer.is_valid(raise_exception=True)

        validated_data = input_serializer.validated_data

        code = validated_data.get('code')
        error = validated_data.get('error')

        login_url = f"{os.environ.get('BASE_FRONTEND_URL')}/login"

        if error or not code:
            params = urlencode({'error':error})
            return redirect(f'{login_url}?{params}')
        
        domain = os.environ.get('BASE_BACKEND_URL')
        redirect_uri = f'{domain}/social_auth/google/'

        access_token = google_get_access_token(code=code,redirect_uri=redirect_uri)

        user_data = google_get_user_info(access_token=access_token)

        profile_data = {
        'email': user_data['email'],
        'first_name': user_data.get('given_name'),
        'last_name': user_data.get('family_name'),
    }

        response = redirect(f"{os.environ.get('BASE_FRONTEND_URL')}/dashboard")
        response.set_cookie('User_data',profile_data, max_age = 60 * 24 * 60 * 60)

        return response
