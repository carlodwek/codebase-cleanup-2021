
# TODO: import some code
from app.shopping import format_usd
from app.shopping import find_product
import os
from pandas import read_csv
# TODO: test the code
def test_format_usd():
    result = format_usd(18.5)
    assert result == "$18.50"
def test_find_product():
    products_filepath = os.path.join(os.path.dirname(__file__), "..", "test", "mock_data/mock_products.csv")
    products_df = read_csv(products_filepath)
    products = products_df.to_dict("records")
    result = find_product(1, products)
    assert result[0]["name"] == "Product 1"
    result = find_product(2, products)
    assert result[0]["name"] == "Product 2"
    result = find_product(3, products)
    assert result[0]["name"] == "Product 3"
    result = find_product(8, products)
    assert result[0]["name"] == "Product 8"
    result = find_product(201, products)
    assert result[0]["name"] == "Product 201"
