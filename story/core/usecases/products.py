from motor.motor_asyncio import AsyncioMotorClient, AsyncIOMotorDatabase
from story.core.db.mongo import db_client
from pydantic import BaseModel
from story.core.schemas.product import ProductUpdate, ProductUpdateOut
from story.core.schemas.products import ProductIn, ProductOut
from story.core.exceptions import NotFoundException
from uuid import UUID
from typing import List
import pymongo

class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncioMotorClient = db_client.get()
        self.database = AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product = ProductOut(**body.model_dump())
        await self.collection.insert_one(**body.model_dump())

        return product

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(f"Product not found with filter: UUID={id}")    

        return ProductOut(**result)
    
    async def query(self) -> list[ProductOut]:
        return [ProductOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_unset=True)},
            return_document=pymongo.ReturnDocument.AFTER
        )

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID):
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(f"Product not found with filter: UUID={id}")    
        
        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False

product_usecase = ProductUsecase()