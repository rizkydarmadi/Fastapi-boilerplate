from fastapi import APIRouter, Depends
from common.responses_schemas import BadRequest, InternalServerError, Forbidden
from common.responses_services import common_response
from .services import Role_permissionServices

router = APIRouter(tags=["role_permission"])

# create endpoints here :)
