
from fastapi import APIRouter, Query, status
from typing import List

from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from app.services.product_service import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product
)


router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)


# API 1: Create Product
@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_product(product_data: ProductCreate):

    return create_product(product_data)


# API 2: Retrieve All Products
@router.get(
    "/",
    response_model=List[ProductResponse],
    status_code=status.HTTP_200_OK
)
def retrieve_all_products(
    category: str | None = Query(default=None),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100)
):

    return get_all_products(
        category=category,
        skip=skip,
        limit=limit
    )


# API 3: Retrieve Product by ID
@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    status_code=status.HTTP_200_OK
)
def retrieve_product(product_id: str):

    return get_product_by_id(product_id)


# API 4: Update Product
@router.put(
    "/{product_id}",
    response_model=ProductResponse,
    status_code=status.HTTP_200_OK
)
def update_existing_product(
    product_id: str,
    product_data: ProductUpdate
):

    return update_product(
        product_id,
        product_data
    )


# API 5: Delete Product
@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_product(product_id: str):

    delete_product(product_id)

    return None
