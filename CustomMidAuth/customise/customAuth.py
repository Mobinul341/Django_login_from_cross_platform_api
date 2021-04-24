from . customException import *

from datetime import datetime, timedelta
#from .models import AuthToken
from django.conf import settings

import logging
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser, User
from django.utils import timezone

class CustomAuth(BaseAuthentication):
    def __init__(self, realm="API"):
        self.realm = realm
    
    def authenticate(self, request, **kwargs):

        try:
            auth_header_value = request.META.get("HTTP_AUTHORIZATION", "")
            if auth_header_value:
                authmeth, auth = request.META["HTTP_AUTHORIZATION"].split(" ",1)
 
                if not auth:
                    return None 
                if not authmeth.lower() == "bearer":
                    return None 
                token = CustomAuth,verify_access_token(request, auth)
                return (token, None)
            else:
                raise ClientNotFound()
        except TokenExpired as tkerr:
            raise TokenExpired()
        except KeyError as kerr:
            request.user = AnonymousUser()
            raise ClientNotFound()


    @staticmethod
    def verify_access_token(request, auth):
        if AuthToken.objects.filter(access_token=auth).exists():
            token = AuthToken.objects.get(access_token=auth)
            user = User.objects.get_or_create(username="Sample User")[0]
            if token.expiry_date < timezone.now():
                token.expired = True
                token.save()
                raise TokenExpired
            return user
        else:
            raise ClientNotFound()


            