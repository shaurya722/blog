from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):

        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('username is exists..')
        
        if User.objects.filter(email=data['email']).exists():
          raise serializers.ValidationError('Email already exists.')


        return data
    

    def create(self,validated_data):
        user = User.objects.create(
        first_name = validated_data['first_name'],
        last_name = validated_data['last_name'],
        email = validated_data['email'],
        username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


    def validate(self,data):
        if not User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('account not found..')

        return data
    
    def get_jwt_token(self,data):
        
        user = authenticate(username = data['username'],
                            password = data['password'])

        if not user:
            return {
                'message':'invalid creadentail',
                'data':{}
            }
        
        refresh = RefreshToken.for_user(user)
        return {
                'message':'login success..',
                'data':{
                    'token': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    }}
            }