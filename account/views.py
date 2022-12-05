from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import RegistrationSerializer


User = get_user_model()


class RegistrationApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully signed up! Please check your email and activate your account.',
                            status=status.HTTP_201_CREATED)


class ActivationApiView(APIView):

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'message': 'Your account successfully activated!'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'This code is incorrect!'}, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordApiView(APIView):
    def post(self, request):
