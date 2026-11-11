from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class Product:
    product_id: str
    product_name: str
    product_description: str | None
    product_price: float
    stock_quantity: int
    product_category: str
    product_status: str
    created_date: datetime


def generate_product_id() -> str:
    return str(uuid4())


# In-memory product storage
products_db: dict[str, Product] = {}