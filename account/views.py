from django.shortcuts import render
from account.email import send_otp_via_email
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, RegisterSerializer  # Assuming RegisterSerializer is the correct serializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)  # Use the correct serializer here

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong..',
                }, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.save()
            # user = User.objects.get()
            send_otp_via_email(user.email)

            return Response({
                'data': {},
                'message': 'User registered successfully.',
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({   
                'data': {},  
                'message': 'Something went wrong..',
            }, status=status.HTTP_400_BAD_REQUEST)
class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)

            if not serializer.is_valid():
                print(f"Validation Errors: {serializer.errors}")  
                return Response({
                    'data': serializer.errors,
                    'message': 'Validation failed.',
                }, status=status.HTTP_400_BAD_REQUEST)

            res = serializer.get_jwt_token(serializer.validated_data)
            print(f"JWT Token Response: {res}")  
            return Response({
                'data': res['data'],
                'message': res['message'],
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Unexpected Error: {e}") 
            return Response({
                'data': {},
                'message': 'Something went wrong.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
