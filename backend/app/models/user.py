import uuid

from enum import Enum

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Enum as SqlEnum

from app.core.database import Base


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    CANDIDATE = "CANDIDATE"


class User(Base):
    __tablename__ = "users"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    roll_number = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    full_name = Column(
        String,
        nullable=False
    )

    password_hash = Column(
        String,
        nullable=False
    )

    role = Column(
        SqlEnum(UserRole),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )