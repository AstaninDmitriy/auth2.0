from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from typing import List
from core.models import db_helper
from .schemas import Product, ProductCreate, ProductUpdate
from .dependencies import product_by_id

router = APIRouter(tags=["Products"], prefix="/products")

@router.get("/", response_model=List[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.session_dependency)
    ):
    return await crud.get_products(session=session)


@router.get("/{product_id}", response_model=Product)
async def get_product(
    product: Product = Depends(product_by_id)
):
    return product

@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)

@router.put("/{product_id}")
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
    ):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update
    )