from fastapi import APIRouter, Depends, Path
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import UUID4
from starlette import status

from middle_earth.db.connection import get_session
from middle_earth.db.models import Character
from middle_earth.schemas import CharacterResponse
from middle_earth.crud import get_character, get_character_id


api_router = APIRouter(tags=["Middle-Earth"])


@api_router.get(
    "/character/{id}",
    status_code=status.HTTP_200_OK,
    response_model=CharacterResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "This page doesn't exist.",
        }
    },
)
async def character(
    id: int,
    session: AsyncSession = Depends(get_session),
):
    character = await get_character_id(session, id)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', character.id)
    return CharacterResponse.from_orm(character)