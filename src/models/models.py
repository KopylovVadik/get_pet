from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True

    convention = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }

    metadata = MetaData(naming_convention=convention)


class Owner(Base):
    __tablename__ = 'owners'

    pk = 'id'

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String, comment='Имя')
    last_name = Column(String, comment='Фамилия')
    phone_number = Column(String, unique=True, comment='Номер телефона')
    email = Column(String, unique=True, comment='Адрес электронной почты')
    telegram = Column(String, unique=True, nullable=True, comment='Телеграм')
    created_at = Column(DateTime, default=func.now())


class Pet(Base):
    __tablename__ = 'pets'

    pk = 'id'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, comment='Кличка')
    birth_date = Column(Date, comment='Дата рождения')
    brand = Column(String, nullable=True, comment='Порода')
    special_feature = Column(String, nullable=True, comment='Особые приметы')
    owner_id = Column(Integer, ForeignKey('owners.id'))
    created_at = Column(DateTime, default=func.now())
