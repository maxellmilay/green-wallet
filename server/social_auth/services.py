import requests
import os
from typing import Dict, Any

from django.core.exceptions import ValidationError

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
        raise ValidationError('Could not get user info frm Google')

    return response.json()
