
from datetime import datetime, timezone
from uuid import UUID

from fastapi import HTTPException, status

from app.models.product_model import (
    Product,
    products_db,
    generate_product_id
)

from app.schemas.product_schema import ProductCreate


def validate_product_id(product_id: str):
    """Validate product ID format."""

    try:
        UUID(product_id)
    except (ValueError, TypeError, AttributeError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid product ID format"
        )


def create_product(product_data: ProductCreate):
    """Create and store a new product."""

    product_id = generate_product_id()

    if product_id in products_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Duplicate product ID"
        )

    product = Product(
        product_id=product_id,
        product_name=product_data.product_name,
        product_description=product_data.product_description,
        product_price=product_data.product_price,
        stock_quantity=product_data.stock_quantity,
        product_category=product_data.product_category,
        product_status=product_data.product_status,
        created_date=datetime.now(timezone.utc)
    )

    products_db[product_id] = product

    return product


def get_all_products(
    category: str | None = None,
    skip: int = 0,
    limit: int = 10
):
    """Retrieve products with optional filtering and pagination."""

    product_list = list(products_db.values())

    if category:
        product_list = [
            product for product in product_list
            if product.product_category.casefold() == category.strip().casefold()
        ]

    return product_list[skip:skip + limit]


def get_product_by_id(product_id: str):
    """Retrieve a product using its ID."""

    validate_product_id(product_id)

    product = products_db.get(product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return product


def update_product(
    product_id: str,
    product_data: ProductCreate
):
    """Update an existing product."""

    validate_product_id(product_id)

    existing_product = products_db.get(product_id)

    if existing_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    updated_product = Product(
        product_id=product_id,
        product_name=product_data.product_name,
        product_description=product_data.product_description,
        product_price=product_data.product_price,
        stock_quantity=product_data.stock_quantity,
        product_category=product_data.product_category,
        product_status=product_data.product_status,
        created_date=existing_product.created_date
    )

    products_db[product_id] = updated_product

    return updated_product


def delete_product(product_id: str):
    """Delete an existing product."""

    validate_product_id(product_id)

    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    del products_db[product_id]

    return None
