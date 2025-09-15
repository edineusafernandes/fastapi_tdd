from dataclasses import Field
from decimal import Decimal
from pydantic import UUID4, model_validator
import datetime 
from typing import Optional
from story.core.schemas.base import BaseSchemaIn
from pydantic import BaseModel
from bson import Decimal128

class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")

class ProductIn(ProductBase, BaseSchemaMixIn): 
    pass

class ProductOut(ProductIn):
    id: UUID4 = Fiel()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    @model_validator
    def set_schema(cls, data):
         for key, value in data.items():
            if isinstance(value, Decimal128):
                data[key] = Decimal(str(value))

            return data

class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[float] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")

class ProductUpdateOut(ProductUpdate):
    quantity: optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")
