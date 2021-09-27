from rest_framework.views import exception_handler
from litap.utils import sendResponse
from requests import ConnectionError
from rest_framework import status


def global_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)



    # # checks if the raised exception is of the type you want to handle
    # if isinstance(exc, ConnectionError):
    #     # defines custom response data
    #     err_data = {'MSG_HEADER': 'some custom error messaging'}

    #     return JsonResponse(err_data, safe=False, status=503)

    # returns response as handled normally by the framework
    return sendResponse(
                        status = False,
                        message= "Bad Request",
                        responseCode = status.HTTP_400_BAD_REQUEST
                            )