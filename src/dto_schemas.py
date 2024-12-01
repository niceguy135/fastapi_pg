from datetime import datetime

from pydantic import BaseModel

from src.models import LanguageOrm


class UsersAddDTO(BaseModel):
    username: str
    language: LanguageOrm


class UsersDTO(UsersAddDTO):
    id: int


class UsersWithAchievements(UsersDTO):
    achievements: list["AchievementsDTO"]


class AchievementsAddDTO(BaseModel):
    title_ru: str
    title_en: str
    description_ru: str
    description_en: str
    value: int


class AchievementsDTO(AchievementsAddDTO):
    id: int


class PresentUserAnAchievement(BaseModel):
    user_id: int
    achievement_id: int


class Translated_achievement(BaseModel):
    translated_title: str
    translated_description: str
    value: int
    present_at: datetime