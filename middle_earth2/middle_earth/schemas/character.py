from pydantic import BaseModel, Field

class CharacterResponse(BaseModel):
    id: int
    name: str
    content: str

    class Config:
        from_attributes = True

