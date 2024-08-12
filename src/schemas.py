from pydantic import BaseModel


class OwnerBaseSchema(BaseModel):
    first_name: str
    last_name: str


class OwnerCreateSchema(OwnerBaseSchema):
    pass


class OwnerReadSchema(OwnerBaseSchema):
    id: int
