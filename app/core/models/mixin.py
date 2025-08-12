from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User



class UserRelationMixin:
    _user_id_unique: bool = False
    _user_back_populates: str | None = None
    _user_id_nullable: bool = False


    @declared_attr
    def user_id(cls):
        return mapped_column(
            ForeignKey("Users.id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable
        )
    
    @declared_attr
    def user(cls):
        return relationship(
            argument = "User",
            back_populates=cls._user_back_populates
        )