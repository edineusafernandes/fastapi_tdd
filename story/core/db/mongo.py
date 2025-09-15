from motor.motor_asyncio import AsyncIOMotorClient
from story.core.config import settings

class MongoClient:
    def __init__(self) -> None:
        self.client: AsyncioMotorClient = AsyncIOMotorClient(settings.DATABASE_URL )

    def get_client(self) -> AsyncIOMotorClient:
        return self.client
    
db_client = MongoClient()
