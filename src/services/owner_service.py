from functools import lru_cache

from fastapi import Depends

from database import db_helper
from repository.base_repository import BaseRepository
from repository.owner_repository import get_owner_repository
from schemas.owner import BaseOwnerSchema
from services.base_service import BaseService, ListService


class OwnersService(BaseService, ListService):
    """ Сервис пользователя """
    schema = BaseOwnerSchema


@lru_cache
def get_owner_service(
        repository: BaseRepository = Depends(get_owner_repository),
) -> OwnersService:
    """Зависимость для сервиса ролей."""
    return OwnersService(repository)
