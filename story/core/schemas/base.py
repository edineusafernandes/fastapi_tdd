import datetime
from uuid import uuid4
from pydantic import BaseModel, UUID4, Field


class BaseSchemaIn(BaseModel):
    id: uuid4 = Field(default_factory=uuid4)
    created_at: str = Field(default_factory=datetime.ucnow)
    updated_at: str = Field(default_factory=datetime.ucnow)