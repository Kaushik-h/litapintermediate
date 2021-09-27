from django.shortcuts import render
from rest_framework import generics, permissions,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from django.core.mail import send_mail
from Auth.models import User,CallbackToken
from Auth.serializers import *
import requests
from rest_framework.response import Response
from litap.utils import sendResponse
from requests.exceptions import HTTPError


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = CallbackToken.objects.create(user = user)
        send_mail(
            subject = 'Verify your Email Address to use litap account.',
            #Must be replaced with varible UI url in settings
            message = f'litap.net?token={token.key}',
            from_email = '',
            recipient_list = [user.primaryEmail],
            fail_silently=False,
            )
        return sendResponse(
                            status = True,
                            message= "Verification Email sent",
                            responseCode = status.HTTP_200_OK,
                            data = {
                                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                                    }
                            )

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return sendResponse(
                        status = True,
                        responseCode = status.HTTP_200_OK,
                        data = {
                                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                                "token": AuthToken.objects.create(user)[1]
                                })

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request._auth.delete()
        return sendResponse(
                            status = True,
                            responseCode = status.HTTP_204_NO_CONTENT
                            )

class LogoutAllView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request.user.auth_token_set.all().delete()
        return sendResponse(status = True,responseCode = status.HTTP_204_NO_CONTENT)

class PasswordchangeView(APIView):
    def post(self, request):
        oldPassword = request.data.get('oldPassword')
        newPassword = request.data.get('newPassword')
        userObj = request.user
        if userObj.check_password(oldPassword):
            userObj.set_password(newPassword)
            userObj.save()
            return sendResponse(status=True,
                                    message="Password Changed successfully",
                                    data= UserSerializer(userObj).data,
                                    responseCode=status.HTTP_204_NO_CONTENT
                                    )
        else:
            return sendResponse(status=False,
                                    message="Wrong credentials",
                                    responseCode=status.HTTP_400_BAD_REQUEST
                                    )

class PasswordResetRequestView(APIView):
    def post(self, request):
        try:
            primaryEmail = request.data.get('primaryEmail')
            user = User.objects.get(primaryEmail = primaryEmail)
            token = CallbackToken.objects.create(user = user)
            send_mail(
                        subject = 'Reset password to your litap account.',
                        #Must be replaced with varible UI url in settings
                        message = f'litap.net?token={token.key}',
                        from_email = '',
                        recipient_list = [primaryEmail],
                        fail_silently=False,
                    )
            return sendResponse(status=True,
                                message="Password reset details sent to email if exists",
                                responseCode=status.HTTP_200_OK
                                )
        except:
            return sendResponse(status=True,
                                message="Password reset details sent to email if exists",
                                responseCode=status.HTTP_200_OK
                                )

class PasswordResetVerifyView(APIView):
    def post(self,request):
        try:
            token = request.data.get('callbackToken')
            Password = request.data.get('Password')
            tokenCheck = CallbackToken.objects.filter(key=token,is_active=True)
            if tokenCheck.exists():
                tokenObj = tokenCheck.last()
                userObj = tokenObj.user
                userObj.set_password(newPassword) 
                userObj.save()
                tokenObj.is_active = False
                tokenObj.save()
                return sendResponse(
                                    status=True,
                                    message="Password reset Successfully",
                                    responseCode=status.HTTP_204_NO_CONTENT
                                    )

            else:
                return sendResponse(
                                status=False,
                                message="Invalid Reset Link",
                                responseCode=status.HTTP_403_FORBIDDEN
                                )
        except:
            return sendResponse(status=False,
                                message="Password Reset Failed",
                                responseCode=status.HTTP_400_BAD_REQUEST
                                )

class SocialSignIn(APIView):
    def post(self,request,backend):
        serializer = SocialSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                nfe = api_settings.NON_FIELD_ERRORS_KEY
            except AttributeError:
                nfe = 'non_field_errors'
            try:
                user = request.backend.do_auth(serializer.validated_data['access_token'])
            except HTTPError as e:
                return Response(
                    {'errors': {
                        'token': 'Invalid token',
                        'detail': str(e),
                    }},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if user:
                sendResponse(
                        status = True,
                        responseCode = status.HTTP_200_OK,
                        data = {
                                "user": UserSerializer(user).data,
                                "token": AuthToken.objects.create(user)[1]
                                })
            else:
                return Response(
                    {'errors': {nfe: "Authentication Failed"}},
                    status=status.HTTP_400_BAD_REQUEST,
                )