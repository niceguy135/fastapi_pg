import enum
import datetime
from typing import Annotated

from sqlalchemy import CheckConstraint, ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


str_100 = Annotated[str, String(100)]
intpk = Annotated[int, mapped_column(primary_key=True)]
present_at = Annotated[datetime.datetime, mapped_column(server_default=text("now()"))]


class LanguageOrm(enum.Enum):
    russian = "ru"
    english = "en"


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[str_100]
    language: Mapped[LanguageOrm]

    received_achievements: Mapped[list["AchievementOrm"]] = relationship(
        back_populates="received_users",
        secondary="users_achievements",
    )


class AchievementOrm(Base):
    __tablename__ = "achievements"

    id: Mapped[intpk]
    title_ru: Mapped[str_100]
    title_en: Mapped[str_100]
    description_ru: Mapped[str]
    description_en: Mapped[str]
    value: Mapped[int]

    received_users: Mapped[list["UsersOrm"]] = relationship(
        back_populates="received_achievements",
        secondary="users_achievements",
    )

    __table_args__ = (
        CheckConstraint("value > 0", name="achievement_value_positive"),
    )


class UsersAchievementsOrm(Base):
    __tablename__ = "users_achievements"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    achievement_id: Mapped[int] = mapped_column(
        ForeignKey("achievements,id", ondelete="CASCADE"),
        primary_key = True,
    )
    present_at: Mapped[present_at]
