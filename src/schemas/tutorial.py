from pydantic import BaseModel, Field


class Error(BaseModel):
    detail: str


class TutorialCreate(BaseModel):
    topic: str = Field(max_length=50)
    category: str
    author: str
