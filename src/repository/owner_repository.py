from functools import lru_cache

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from models.models import Owner
from repository.base_repository import CrudRepository


class OwnerRepository(CrudRepository):
    """ Репозиторий для ролей """

    model = Owner


@lru_cache
def get_owner_repository(
        session: AsyncSession = Depends(db_helper.session_getter),
) -> OwnerRepository:
    """Получение репозитория ролей."""
    return OwnerRepository(session)
