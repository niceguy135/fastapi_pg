import datetime

from sqlalchemy import insert, select, text

from app.src.database import async_session_factory, async_engine
from app.src.models import UsersOrm, AchievementOrm, UsersAchievementsOrm, LanguageOrm
from app.src import dto_schemas as DTO


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
                    {
                        "title_ru": "Прыжки с места 200м - призер",
                        "title_en": "Jumping from a place 200m - laureate",
                        "description_ru": "Данное достижение выдается спортсмену, попавшему в топ результатов участников в состязании на прыжок в длину с места на дистанции 200 метров",
                        "description_en": "This achievement is given to the athlete who is in the top of the results of the participants in the long jump competition from a place for a distance of 200 meters",
                        "value": 30
                    },
                    {
                        "title_ru": "Прыжки в высоту - призер",
                        "title_en": "High jump - laureate",
                        "description_ru": "Данное достижение выдается спортсмену, попавшему в топ результатов участников в состязании по прыжкам в высоту",
                        "description_en": "This achievement is given to the athlete who is in the top of the results of the participants in the high jump competition",
                        "value": 20
                    },
                    {
                        "title_ru": "Прыжки в длину - чемпион",
                        "title_en": "Long jump - champion",
                        "description_ru": "Данное достижение выдается спортсмену, занявшему первое место в соревнованиях по прыжкам в длину",
                        "description_en": "This achievement is awarded to the athlete who took first place in the long jump competition",
                        "value": 50
                    },
                    {
                        "title_ru": "Многоборье - финалист",
                        "title_en": "Decathlon - finalist",
                        "description_ru": "Данное достижение выдается спортсмену, вошедшему в финал соревнований по многоборью",
                        "description_en": "This achievement is given to the athlete who reached the final of the decathlon competition",
                        "value": 40
                    },
                    {
                        "title_ru": "Тройной прыжок - победитель",
                        "title_en": "Triple jump - winner",
                        "description_ru": "Данное достижение выдается спортсмену, занявшему первое место в соревнованиях по тройному прыжку",
                        "description_en": "This achievement is given to the athlete who took first place in the triple jump competition",
                        "value": 45
                    },
                    {
                        "title_ru": "Прыжки с места 50м - участник",
                        "title_en": "Jumping from a place 50m - participant",
                        "description_ru": "Данное достижение выдается каждому спортсмену, принявшему участие в соревнованиях на прыжок в длину с места на дистанции 50 метров",
                        "description_en": "This achievement is given to every athlete who participated in the long jump competition from a place for a distance of 50 meters",
                        "value": 10
                    },
                    {
                        "title_ru": "Прыжки в длину - призер",
                        "title_en": "Long jump - laureate",
                        "description_ru": "Данное достижение выдается спортсмену, попавшему в топ результатов участников в соревнованиях по прыжкам в длину",
                        "description_en": "This achievement is given to the athlete who is in the top of the results of the participants in the long jump competition",
                        "value": 35
                    },
                    {
                        "title_ru": "Прыжки в высоту - участник",
                        "title_en": "High jump - participant",
                        "description_ru": "Данное достижение выдается каждому спортсмену, принявшему участие в соревнованиях по прыжкам в высоту",
                        "description_en": "This achievement is given to every athlete who participated in the high jump competition",
                        "value": 15
                    }
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

    @staticmethod
    async def _insert_sample_seven_days_in_row_achievs():
        async with async_session_factory() as session:
            user_query = select(UsersOrm).where(UsersOrm.id == 3)

            winner_achives_query = select(AchievementOrm).where(AchievementOrm.value == 50)

            user = await session.scalar(user_query)
            achiev = (await session.scalars(winner_achives_query)).first()

            for extra_day in range(9):
                session.add(
                    UsersAchievementsOrm(
                        user_id=user.id,
                        achievement_id=achiev.id + 2 + extra_day,
                        present_at=datetime.datetime.now() - datetime.timedelta(days=extra_day)
                    )
                )

            await session.commit()

    @classmethod
    async def insert_sample_data(cls):
        await cls._insert_sample_users()
        await cls._insert_sample_achievements()
        await cls._insert_sample_achievements_presents()
        await cls._insert_sample_seven_days_in_row_achievs()


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

    @staticmethod
    async def _get_user_max_achievs_count():
        async with async_engine.connect() as conn:
            max_achievements_count_user_query = text(
                f"""SELECT 
                    u.id AS user_id, 
                    u.username, 
                    COUNT(ua.achievement_id) AS achievement_count
                FROM 
                    {UsersOrm.__tablename__} u
                JOIN 
                    {UsersAchievementsOrm.__tablename__} ua 
                    ON u.id = ua.user_id
                GROUP BY 
                    u.id, u.username
                ORDER BY 
                    achievement_count DESC
                LIMIT 1;
                """
            )
            user_id, username, count = (await conn.execute(max_achievements_count_user_query)).first()

            return DTO.UserMaxAchievementsCount(
                user_id=user_id,
                username=username,
                achievements_count=count
            )

    @staticmethod
    async def _get_user_max_achievs_point():
        async with async_engine.connect() as conn:
            user_with_max_points_query = text(
                f"""
                SELECT 
                    u.id AS user_id, 
                    u.username, 
                    SUM(a.value) AS total_points
                FROM 
                    {UsersOrm.__tablename__} u
                JOIN 
                    {UsersAchievementsOrm.__tablename__} ua 
                    ON u.id = ua.user_id
                JOIN 
                    {AchievementOrm.__tablename__} a 
                    ON ua.achievement_id = a.id
                GROUP BY 
                    u.id, u.username
                ORDER BY 
                    total_points DESC
                LIMIT 1;
                """
            )
            user_id, username, points = (await conn.execute(user_with_max_points_query)).first()

            return DTO.UserMaxPoints(
                user_id=user_id,
                username=username,
                user_points=points
            )

    @staticmethod
    async def _get_users_max_point_diff():
        async with async_engine.connect() as conn:
            users_with_max_diff_by_points = text(
                f"""
                WITH user_points AS (
                    SELECT 
                        u.id AS user_id, u.username as username,
                        SUM(a.value) AS total_points
                    FROM 
                        {UsersOrm.__tablename__} u
                    JOIN 
                        {UsersAchievementsOrm.__tablename__} ua 
                        ON u.id = ua.user_id
                    JOIN 
                        {AchievementOrm.__tablename__} a 
                        ON ua.achievement_id = a.id
                    GROUP BY 
                        u.id
                )
                SELECT 
                    up1.user_id AS user1_id,
                    up2.user_id AS user2_id,
                    ABS(up1.total_points - up2.total_points) AS points_difference
                FROM 
                    user_points up1
                CROSS JOIN 
                    user_points up2
                WHERE 
                    up1.user_id < up2.user_id
                ORDER BY 
                    points_difference DESC
                LIMIT 1;
                """
            )
            user_id_first, user_id_second, points = (await conn.execute(users_with_max_diff_by_points)).first()

            return DTO.UsersWithDiffPoints(
                user_id_first=user_id_first,
                user_id_second=user_id_second,
                points=points
            )

    @staticmethod
    async def _get_users_min_point_diff():
        async with async_engine.connect() as conn:
            users_with_min_diff_by_points = text(
                f"""
                WITH user_points AS (
                    SELECT 
                        u.id AS user_id, 
                        SUM(a.value) AS total_points
                    FROM 
                        {UsersOrm.__tablename__} u
                    JOIN 
                        {UsersAchievementsOrm.__tablename__} ua 
                        ON u.id = ua.user_id
                    JOIN 
                        {AchievementOrm.__tablename__} a 
                        ON ua.achievement_id = a.id
                    GROUP BY 
                        u.id
                )
                SELECT 
                    up1.user_id AS user1_id,
                    up2.user_id AS user2_id,
                    ABS(up1.total_points - up2.total_points) AS points_difference
                FROM 
                    user_points up1
                CROSS JOIN 
                    user_points up2
                WHERE 
                    up1.user_id < up2.user_id
                ORDER BY 
                    points_difference ASC
                LIMIT 1;
                """
            )
            user_id_first, user_id_second, points = (
                await conn.execute(users_with_min_diff_by_points)).first()

            return DTO.UsersWithDiffPoints(
                user_id_first=user_id_first,
                user_id_second=user_id_second,
                points=points
            )

    @staticmethod
    async def _get_user_seven_days_in_row():
        async with async_engine.connect() as conn:
            user_get_achievs_for_seven_days_in_row = text(
                f"""
                                WITH user_achievement_days AS (
                    SELECT 
                        ua.user_id, 
                        ua.present_at AS achievement_date
                    FROM 
                        {UsersAchievementsOrm.__tablename__} ua
                    GROUP BY 
                        ua.user_id, ua.present_at
                ),
                consecutive_days AS (
                    SELECT 
                        user_id, 
                        achievement_date, 
                        EXTRACT(DAY FROM now()-achievement_date) AS streak_group
                    FROM 
                        user_achievement_days
                ),
                streak_counts AS (
                    SELECT 
                        user_id, 
                        COUNT(*) AS streak_length
                    FROM 
                        consecutive_days
                    GROUP BY 
                        user_id, streak_group
                ),
                totalcount as (
				SELECT 
                    u.id AS user_id, 
                    u.username, count(u.id)
                FROM 
                    streak_counts sc
                JOIN 
                    {UsersOrm.__tablename__} u ON sc.user_id = u.id
				group by u.id
				)
				select *
				from totalcount
				where count > 1
                """
            )

            users = (await conn.execute(user_get_achievs_for_seven_days_in_row)).all()
            all_users_dto = []
            for user in users:
                all_users_dto.append(
                    DTO.UsersDTO(
                        username=user.username if user is not None else "No user",
                        language=LanguageOrm.russian,
                        id=user.user_id if user is not None else -1,
                    )
                )

            return all_users_dto

    @classmethod
    async def get_statistics_data(cls):
        max_achieve_count = await cls._get_user_max_achievs_count()
        max_achiev_point = await cls._get_user_max_achievs_point()
        max_diff_points = await cls._get_users_max_point_diff()
        min_diff_points = await cls._get_users_min_point_diff()
        seven_days_in_row = await cls._get_user_seven_days_in_row()

        return DTO.StatisticScheme(
            user_max_achievements_count=max_achieve_count,
            user_max_achievements_points=max_achiev_point,
            users_with_max_diff=max_diff_points,
            users_with_min_diff=min_diff_points,
            user_seven_days_in_row=seven_days_in_row
        )
