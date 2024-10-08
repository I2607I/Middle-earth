from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from middle_earth.endpoints.main import character

router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='templates')


@router.get('/characters/{id}')
async def get_students_html(request: Request, character=Depends(character)):
    return templates.TemplateResponse(name='character.html',
                                      context={'request': request, 'character': character})