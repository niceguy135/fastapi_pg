from pydantic import BaseModel

from models import LanguageOrm


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
