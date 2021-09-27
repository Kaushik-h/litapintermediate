from rest_framework.response import Response
from rest_framework import status
from Auth.models import User
from django.conf import settings

def sendResponse(status,responseCode,data=None,message=None):
    return Response(
        {
            'status':status, 
            'message':message, 
            'data' : data if data else ''
            },
            status= responseCode if responseCode else status.HTTP_200_OK
                            )

def deleted_user():
    DELETED_GUEST_EMAIL = 'unknown-user@unknown.com'
    """ used for setting the user field of a review when user is deleted """
    deleted_user_obj, created = User.objects.get_or_create(
        username = 'Unknown',
        first_name='Unknown',
        last_name='User',
        primaryEmail = DELETED_GUEST_EMAIL, 
        isTribeLeader=False,
        isModerator=False
    )
    return deleted_user_obj