import os
import jwt

from django.shortcuts import redirect
from django.db.models import Q, Sum

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from .services import create_jwt_token, get_user_data
from .serializers import InputSerializer, GoogleUserSerializer
from .models import GoogleUser

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer

class GoogleSocialAuthView(APIView):
    def get(self, request):
        input_serializer = InputSerializer(data=request.GET)
        input_serializer.is_valid(raise_exception=True)

        validated_data = input_serializer.validated_data
        jwt_token = create_jwt_token(validated_data)

        response = redirect(f"{os.environ.get('BASE_FRONTEND_URL')}/dashboard")
        response.set_cookie('Token',jwt_token, max_age = 60 * 24 * 60 * 60)

        return response

class GetUserData(RetrieveAPIView):
    def get(self,request):
        email = get_user_data(request)
        # pylint: disable=E1101
        user = GoogleUser.objects.get(email=email)

        transactions = Transaction.objects.filter(group__owner__email=email)
        if transactions.count() != 0:
            user.income = transactions.aggregate(value=Sum('amount',filter=Q(amount__gt=0))).get('value')
            user.expenses = transactions.aggregate(value=Sum('amount',filter=Q(amount__lt=0))).get('value')
            if user.income is None:
                user.income = 0
                user.balance = user.expenses
            if user.expenses is None:
                user.expenses = 0
                user.balance = user.income
            if user.expenses is not None and user.income is not None:
                user.balance = transactions.aggregate(value=Sum('amount')).get('value')
            user.save()

        serializer = GoogleUserSerializer(user)

        return Response(serializer.data)
        
