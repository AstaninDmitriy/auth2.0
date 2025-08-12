from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixin import UserRelationMixin



class Profile(UserRelationMixin, Base):
    __tablename__ = "Profiles"
    _user_id_unique = True
    _user_back_populates = "profile"
    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]

