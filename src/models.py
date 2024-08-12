from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer, DateTime, Date, func, ForeignKey, MetaData


class Base(DeclarativeBase):
    __abstract__ = True


class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String, comment='Имя')
    last_name = Column(String, comment='Фамилия')
    phone_number = Column(String, unique=True, comment='Номер телефона')
    email = Column(String, unique=True, comment='Адрес электронной почты')
    telegram = Column(String, unique=True, nullable=True, comment='Телеграм')
    created_at = Column(DateTime, default=func.now())


class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, comment='Кличка')
    birth_date = Column(Date, comment='Дата рождения')
    brand = Column(String, nullable=True, comment='Порода')
    special_feature = Column(String, nullable=True, comment='Особые приметы')
    owner_id = Column(Integer, ForeignKey('owners.id'))
    created_at = Column(DateTime, default=func.now())
