import datetime

from .base_schema import BaseSchema


class BaseOwnerSchema(BaseSchema):
    """Схема для ролей."""

    id: int
    first_name: str
    last_name: str
    phone_number: str
    email: str
    telegram: str


class ReadOwnerSchema(BaseOwnerSchema):
    """ Схема получения пользователя """
    created_at: datetime.datetime


class CreateOwnerSchema(BaseOwnerSchema):
    """ Схема для создания пользователя  """

    ...


class UpdateOwnerSchema(BaseOwnerSchema):
    """ Схема для обновления пользователя """

    ...
