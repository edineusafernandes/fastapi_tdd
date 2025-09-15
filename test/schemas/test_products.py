from uuid import UUID
from story.core.schemas.product import ProductIn
from pydantic import ValidationError
from test.schemas.factories import product_data

def test_schemas_return_sucssess():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Pano da Costa"
    assert isinstance(product.id, UUID)

def test_schemas_return_raise():
    data = {'name': 'Pano da Costa', 'quantity': 10, 'price': 780, 'status': True}
            
    with pytest.raises(ValidationError):
    product = ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        'type':'missing', 
        'loc':('id',), 
        'msg':'Field required', 
        'input': {'name': 'Pano da Costa', 'quantity': 10, 'price': 780, 'status': True}}