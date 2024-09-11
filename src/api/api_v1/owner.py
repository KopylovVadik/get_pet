from fastapi import APIRouter
from fastapi import Depends

from schemas.owner import ReadOwnerSchema

from services.owner_service import OwnersService, get_owner_service
from utils.pagination import Paginator

router = APIRouter(
    prefix="/v1/owners",
    tags=["Owners"],
)


@router.get("/", response_model=list[ReadOwnerSchema])
async def get_users(owner_service: OwnersService = Depends(get_owner_service),
                    pagination: Paginator = Depends(Paginator)) -> list[ReadOwnerSchema]:
    """ Получение списка пользователей """

    users = await owner_service.get_all(pagination, ('id',))
    return users
