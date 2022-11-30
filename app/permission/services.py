from .repository import PermissionRepository
from .model import Permission
from common.responses_services import BadRequest, Created, InternalServerError, Ok
from common.security import generate_jwt_token_from_user


class PermissionServices:
    pass  # add your services here :`)
