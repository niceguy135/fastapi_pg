from pydantic import BaseModel

from models import LanguageOrm


class UsersAddDTO(BaseModel):
    username: str
    language: LanguageOrm


class UsersDTO(UsersAddDTO):
    id: int
