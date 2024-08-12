from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from models import Owner
from schemas import OwnerReadSchema

router = APIRouter(
    prefix="/v1/users",
    tags=["Owners"],
)


@router.get("/", response_model=list[OwnerReadSchema])
async def get_users(session: AsyncSession = Depends(db_helper.session_getter)):
    stmt = select(Owner).order_by(Owner.id)
    result = await session.scalars(stmt)
    return result.all()
