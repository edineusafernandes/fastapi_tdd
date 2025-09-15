from dataclasses import Field
from decimal import Decimal
from typing import Any
from uuid import uuid4
from pydantic import BaseModel, UUID4, model_serializer
from bson import Decimal128
from datetime import datetime


class CreatedBaseModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @model_serializer
    def set_model(self) -> dict[str, Any]:
        self_dict = dict(self)

        for key, value in self_dict.items():
            if isinstance(value, Decimal):
                self_dict[key] = Decimal128(str(value))

            return self_dict