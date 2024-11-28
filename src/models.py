import enum
from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column

from database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class LanguageOrm(enum.Enum):
    russian = "ru"
    english = "en"


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str]
    language: Mapped[LanguageOrm]
