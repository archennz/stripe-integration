import pytest
from src.main import create_customer, create_invoice

@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["authorization"]}

@pytest.mark.vcr
def test_single():
    assert True == True
    customer_id = create_customer("test_2", "test_2@gmail.com")
    invoice = create_invoice(customer_id)