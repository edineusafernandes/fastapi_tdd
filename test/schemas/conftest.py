import asyncio
from uuid import UUID
import pytest
from story.core.db.mongo import db_client
from story.core.schemas.product import ProductIn, ProductUpdate
from test.schemas.factories import product_data
from story.core.usecases.products import product_usecase

@pytest.fixture(scope="session")
def event_loop():
    loop.asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture 
def mongo_client():
    return db_client.get()

@pytest.fixture(autouse=True)
async def clear_collections_names():
    yield
    collections_names = await mongo_client.get_database().list_collections_names()
    for collection_name in collections_names:
        if collection_name.startswith("system"):
            continue

        await mongo_client.get_database()[collection_name].delete_many({})

@pytest.fixture
def product_id():
    return UUID("{fce6cc37-1809-4a8e-a8b2-977df327801a}")

@pytest.fixture
def product_in():
    return ProductIn(**product_data())


@pytest.fixture
def product_up(product_id):
    return ProductUpdate(**product_data(), id=product_id)

@pytest.fixture
async def product_inserted(product_in):
    return await product_usecase.create(body=product_in) 

