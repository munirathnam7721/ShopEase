from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Literal
from datetime import datetime


class ProductCreate(BaseModel):

    product_name: str = Field(
        min_length=1,
        max_length=100
    )

    product_description: str | None = Field(
        default=None,
        max_length=500
    )

    product_price: float = Field(
        gt=0,
        allow_inf_nan=False
    )

    stock_quantity: int = Field(
        ge=0,
        strict=True
    )

    product_category: str = Field(
        min_length=1,
        max_length=50
    )

    product_status: Literal["Active", "Inactive"] = "Active"

    @field_validator("product_name")
    @classmethod
    def validate_product_name(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Product name cannot be empty")

        return value

    @field_validator("product_category")
    @classmethod
    def validate_product_category(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Product category cannot be empty")

        return value

    @field_validator("product_description")
    @classmethod
    def validate_description(cls, value):
        if value is not None:
            value = value.strip()

            if not value:
                return None

        return value


class ProductUpdate(ProductCreate):
    pass


class ProductResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    product_id: str
    product_name: str
    product_description: str | None
    product_price: float
    stock_quantity: int
    product_category: str
    product_status: str
    created_date: datetime