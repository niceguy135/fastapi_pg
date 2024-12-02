from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.src.models import LanguageOrm


class UsersAddDTO(BaseModel):
    """
    Схема данных для создания пользователя
    """
    username: str
    language: LanguageOrm


class UsersDTO(UsersAddDTO):
    """
        Схема данных для получения пользователя из БД
    """
    id: int


class UsersWithAchievements(UsersDTO):
    """
        Схема данных для получения пользователя из БД со списком достижений
    """
    achievements: list["AchievementsDTO"]


class AchievementsAddDTO(BaseModel):
    """
        Схема данных для создания нового достижения
    """
    title_ru: str
    title_en: str
    description_ru: str
    description_en: str
    value: int


class AchievementsDTO(AchievementsAddDTO):
    """
        Схема данных для получения достижения из БД
    """
    id: int


class PresentUserAnAchievement(BaseModel):
    """
        Схема данных для награждения пользователя достижением
    """
    user_id: int
    achievement_id: int


class Translated_achievement(BaseModel):
    """
        Схема данных для получения информации о полученных достижениях пользователя на его выбранном языке
    """
    translated_title: str
    translated_description: str
    value: int
    present_at: datetime


class UserMaxAchievementsCount(BaseModel):
    """
        Схема данных для получения информации о пользователе с максимальным количеством достижений
    """
    user_id: int
    username: str
    achievements_count: int


class UserMaxPoints(BaseModel):
    """
        Схема данных для получения информации о пользователе с максимальным балом за достижений
    """
    user_id: int
    username: str
    user_points: int


class UsersWithDiffPoints(BaseModel):
    """
        Схема данных для получения информации о пользователях с максимальной разницей в баллах
    """
    user_id_first: int
    user_id_second: int
    points: int


class StatisticScheme(BaseModel):
    """
        Схема данных для получения информации о пользователях с минимальной разницей в баллах
    """
    user_max_achievements_count: UserMaxAchievementsCount
    user_max_achievements_points: UserMaxPoints
    users_with_max_diff: UsersWithDiffPoints
    users_with_min_diff: UsersWithDiffPoints
    user_seven_days_in_row: List[UsersDTO]