from ast import List
from uuid import UUID
from story.core.schemas.product import ProductUpdateOut
from story.usecases.products import ProductUsecase
from story.core.usecases.products import product_usecase
from story.core.exceptions import NotFoundException
import pytest
from test.schemas.conftest import product_id

async def test_usecases_should_return_success():
    result = await ProductUsecase.create(body=product_in())

    assert isinstance(result. ProductOut)
    assert result.name == "Pano da Costa"

async def test_usecases_get_should_return_success(product_inserted):
    result = await product_usecase.create.get(id=product_inserted.id)

    assert isinstance(result. ProductOut)
    assert result.name == "Pano da Costa"

async def test_usecases_get_should_return_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("1e4f214c-8577-461a-890a-751a32e3bb9f"))

        assert err.value.message == "Product not found with filter: UUID=1e4f214c-8577-461a-890a-751a32e3bb9f"

async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

async def test_usecases_update_should_return_success(product_up, product_inserted):
    product_up.price = "780.00"
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)

@pytest.mark.usefixtures("product_inserted")
async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1
    
async def test_usecases_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True

async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("1e4f214c-8577-461a-890a-751a32e3bb9f"))

        assert err.value.message == "Product not found with filter: UUID=1e4f214c-8577-461a-890a-751a32e3bb9f"