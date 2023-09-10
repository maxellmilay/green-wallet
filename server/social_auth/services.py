import requests
import os
import jwt

from typing import Dict, Any

from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.contrib.auth.models import User

from .models import GoogleUser

from urllib.parse import urlencode

GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'

def google_get_access_token(*,code:str, redirect_uri:str) -> str:
    data = {
        'code': code,
        'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
        'client_secret': os.environ.get('GOOGLE_CLIENT_SECRET'),
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }

    response = requests.post(GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)

    if not response.ok:
        raise ValidationError("Failed to obtain access token from Google")
    
    access_token = response.json()['access_token']

    return access_token

def google_get_user_info(*, access_token:str) -> Dict[str,Any]:
    response = requests.get(GOOGLE_USER_INFO_URL,params={'access_token':access_token})

    if not response.ok:
        raise ValidationError('Could not get user info from Google')
    
    user_data = response.json()

    return user_data

def create_jwt_token(validated_data):
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
    'given_name': user_data.get('given_name'),
    'family_name': user_data.get('family_name'),
    'picture': user_data.get('picture')
    }

    # Register/Update user in Django Admin
    if not User.objects.filter(username=profile_data['email']).exists():
        user = User.objects.create_user(profile_data['email'],email=profile_data['email'],password=None,first_name=profile_data['given_name'],last_name=profile_data['family_name'])
        user.save()
    else:
        user = User.objects.get(username=profile_data['email'])
        user.username = profile_data['email']
        user.email = profile_data['email']
        user.first_name = profile_data['given_name']
        user.last_name = profile_data['family_name']
        user.save()

    # Register/Update user in PostgreSQL db
    # pylint: disable=E1101
    if not GoogleUser.objects.filter(email=profile_data['email']).exists():
        user = GoogleUser(first_name=profile_data['given_name'],last_name=profile_data['family_name'],email=profile_data['email'],picture=profile_data['picture'])
        user.save()
    else:
        # pylint: disable=E1101
        user = GoogleUser.objects.get(email=profile_data['email'])
        user.first_name = profile_data['given_name']
        user.last_name = profile_data['family_name']
        user.email = profile_data['email']
        user.picture = profile_data['picture']
        user.save()

    jwt_token = jwt.encode(profile_data,os.environ.get('SECRET_KEY'), algorithm="HS256")

    return jwt_token

def validate_jwt_token(jwt_token):
    return jwt.decode(jwt_token, os.environ.get('SECRET_KEY'), algorithms=['HS256'])

def get_user_data(request):
    jwt_data = validate_jwt_token(request.headers.get('Authorization').split(' ')[1])
    return jwt_data['email']
