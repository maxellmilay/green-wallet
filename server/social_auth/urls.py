from django.urls import path

from .views import GoogleSocialAuthView, GetUserData

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),
    path('user/', GetUserData.as_view())
]

