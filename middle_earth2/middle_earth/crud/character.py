from middle_earth.db.models import Character
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import create_engine
from middle_earth.db import Base
from sqlalchemy.orm import Session
import os
import datetime



def get_usuall_session():
    engine = create_engine("postgresql+psycopg2://user:hackme@localhost/middle_earth")
    Base.metadata.create_all(engine)
    session = Session(engine)
    return session



#word
async def create_character(session, name, content=None):
    print(555555555555555555555555555555)
    print()
    print()
    print(name, content)
    character_query = select(Character).where(name==Character.name)
    character = await session.scalar(character_query)
    new_character = None
    if not character:
        t = datetime.datetime.now()
        new_character = Character(name=name, content=content, dt_created=t, dt_updated=t)
        print(666666666666666666666, '\n', '\n')
        print(new_character)
        print(new_character.name)
        session.add(new_character)
        await session.commit()
        await session.refresh(new_character)
    return new_character

async def get_character(session, name):
    character_query = select(Character).where(name==Character.name)
    character = await session.scalars(character_query)
    return character

async def get_character_id(session, id):
    character_query = select(Character).where(id==Character.id)
    character = await session.scalar(character_query)
    return character


# print(datetime.datetime.now())
# name = 'Гендальф'
# content = 'Один из пяти истари, прибывших в Средиземье в Вторую Эпоху'
# print(create_character(session, name, content))

