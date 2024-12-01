from datetime import datetime
from typing import List

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


class UserMaxAchievementsCount(BaseModel):
    user_id: int
    username: str
    achievements_count: int


class UserMaxPoints(BaseModel):
    user_id: int
    username: str
    user_points: int


class UsersWithDiffPoints(BaseModel):
    user_id_first: int
    first_username: str
    user_id_second: int
    second_username: str
    points: int


class StatisticScheme(BaseModel):
    user_max_achievements_count: UserMaxAchievementsCount
    user_max_achievements_points: UserMaxPoints
    users_with_max_diff: UsersWithDiffPoints
    users_with_min_diff: UsersWithDiffPoints
    user_seven_days_in_row: List[UsersDTO]