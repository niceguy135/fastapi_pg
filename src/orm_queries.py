from sqlalchemy import insert, select, text

from src.database import async_session_factory, async_engine
from src.models import UsersOrm, AchievementOrm, UsersAchievementsOrm, LanguageOrm
from src import dto_schemas as DTO


class AsyncUtilsQueries:

    @staticmethod
    async def _insert_sample_users():
        async with async_engine.connect() as conn:
            await conn.execute(
                insert(UsersOrm),
                [
                    {"username": "Борисов Кирилл", "language": LanguageOrm.russian},
                    {"username": "Jon Doe", "language": LanguageOrm.english},
                    {"username": "Ванька Встанька", "language": LanguageOrm.russian},
                ],
            )
            await conn.commit()

    @staticmethod
    async def _insert_sample_achievements():
        async with async_engine.connect() as conn:
            await conn.execute(
                insert(AchievementOrm),
                [
                    {
                        "title_ru": "Бег 100м - победитель",
                        "title_en": "100m running - winner",
                        "description_ru": "Данное достижение выдается спортсмену, победившему в состязании на бег 100м",
                        "description_en": "This achievement is awarded to the sportsman who wins the 100m running competition",
                        "value": 50
                    },
                    {
                        "title_ru": "Бег 100м - призер",
                        "title_en": "100m running - laureate",
                        "description_ru": "Данное достижение выдается спортсмену, попавшему в топ результатов участников в состязании на бег 100м",
                        "description_en": "This achievement is given to the athlete who is in the top of the results of the participants in the 100m running competition",
                        "value": 25
                    },
                    {
                        "title_ru": "Прыжки с места 100м - победитель",
                        "title_en": "Jumping from a place - winner",
                        "description_ru": "Данное достижение выдается спортсмену, победившему в состязании прыжок в длину с места",
                        "description_en": "This achievement is awarded to the athlete who wins the long jump competition from a place",
                        "value": 50
                    },
                    {
                        "title_ru": "Прыжки с места 100м - призер",
                        "title_en": "Jumping from a place - laureate",
                        "description_ru": "Данное достижение выдается спортсмену, попавшему в топ результатов участников в состязании на прыжок в длину с места",
                        "description_en": "This achievement is given to the athlete who is in the top of the results of the participants in the long jump competition from a place",
                        "value": 25
                    },
                ],
            )
            await conn.commit()

    @staticmethod
    async def _insert_sample_achievements_presents():
        async with async_session_factory() as session:
            user_eng_query = select(UsersOrm).where(UsersOrm.language == LanguageOrm.english)
            user_ru_query = select(UsersOrm).where(UsersOrm.language == LanguageOrm.russian)

            winner_achives_query = select(AchievementOrm).where(AchievementOrm.value == 50)

            user_ru = await session.scalar(user_ru_query)
            user_eng = await session.scalar(user_eng_query)
            achievs = await session.scalars(winner_achives_query)

            for user, achiev in zip([user_ru, user_eng], achievs):
                session.add(
                    UsersAchievementsOrm(
                        user_id=user.id,
                        achievement_id=achiev.id
                    )
                )

            await session.commit()

    @classmethod
    async def insert_sample_data(cls):
        await cls._insert_sample_users()
        await cls._insert_sample_achievements()
        await cls._insert_sample_achievements_presents()


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

    @staticmethod
    async def take_users_achievements(user_id: int):
        async with async_session_factory() as session:
            query = (
                select(AchievementOrm, text("present_at"))
                .select_from(UsersAchievementsOrm)
                .join(AchievementOrm, AchievementOrm.id == UsersAchievementsOrm.achievement_id)
                .where(UsersAchievementsOrm.user_id == user_id)
            )

            user: UsersOrm = await session.scalar(select(UsersOrm).where(UsersOrm.id == user_id))
            achievements = await session.execute(query)
            prepared_dtos = []
            for achiev, present_time in achievements:
                print(achiev)
                prepared_dtos.append(
                    DTO.Translated_achievement(
                        translated_title=achiev.title_ru if user.language == LanguageOrm.russian else achiev.title_en,
                        translated_description=achiev.description_ru if user.language == LanguageOrm.russian
                                                                                            else achiev.description_en,
                        value=achiev.value,
                        present_at=present_time
                    )
                )
            return prepared_dtos
