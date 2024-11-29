import enum
from typing import Annotated

from sqlalchemy import CheckConstraint, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
str_100 = Annotated[str, String(100)]


class LanguageOrm(enum.Enum):
    russian = "ru"
    english = "en"


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str_100]
    language: Mapped[LanguageOrm]


class AchievementOrm(Base):
    __tablename__ = "achievements"

    id: Mapped[intpk]
    title_ru: Mapped[str_100]
    title_en: Mapped[str_100]
    description_ru: Mapped[str]
    description_en: Mapped[str]
    value: Mapped[int]

    __table_args__ = (
        CheckConstraint("value > 0", name="achievement_value_positive"),
    )
