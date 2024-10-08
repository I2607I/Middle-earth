from typing import Optional
from pydantic import BaseModel, Field

class CharacterResponse(BaseModel):
    name: str
    content: Optional[str] = None

    class Config:
        from_attributes = True

class CharacterRequest(BaseModel):
    name: str
    content: Optional[str] = None

