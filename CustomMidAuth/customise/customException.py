from rest_framework.exceptions import (
    APIException,
    NotFound,
    PermissionDenied,
    NotAuthenticated
)

class TokenExpired(NotAuthenticated):
    status = 403
    default_detail = "Token has Expired"
    default_code = "Forbidden" 

class ClientNotFound(NotAuthenticated):
    status = 403
    default_detail = "Client not found"
    default_code = "Forbidden"

