from select import select

from src.database import async_session_factory
from src.models import UsersOrm, AchievementOrm, UsersAchievementsOrm
from src import dto_schemas as DTO


class AsyncMainQueries:

    @staticmethod
    async def get_user(user_id: int):
        async with async_session_factory() as session:
            user = await session.get(UsersOrm, user_id)
            return DTO.UsersDTO.model_validate(user, from_attributes=True)


    @staticmethod
    async def get_all_achievements():
        async with async_session_factory() as session:
            query = select(AchievementOrm)
            result = await session.execute(query)
            achievements = result.scalars().all()
            return [DTO.AchievementsDTO.model_validate(row, from_attributes=True) for row in achievements]


    @staticmethod
    async def create_new_achievement(new_achievement: DTO.AchievementsAddDTO):
        async with async_session_factory() as session:
            new_achiv_model = AchievementOrm(
                title_ru=new_achievement.title_ru,
                title_en=new_achievement.title_en,
                description_ru=new_achievement.description_ru,
                description_en=new_achievement.description_en,
                value=new_achievement.value
            )
            session.add(new_achiv_model)
            await session.commit()


    @staticmethod
    async def give_achievement_to_user(user_id: int, achiev_id: int):
        async with async_session_factory() as session:
            new_achiv_user_record = UsersAchievementsOrm(
                user_id=user_id,
                achievement_id=achiev_id
            )
            session.add(new_achiv_user_record)
            await session.commit()
