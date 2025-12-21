from fastapi import APIRouter

from internal.adapter.repo.material_type_repo import MaterialTypeRepo
from internal.adapter.repo.product_type_repo import ProductTypeRepo
from internal.adapter.repo.product_workshops_repo import ProductWorkshopsRepo
from internal.adapter.repo.products_repo import ProductsRepo
from internal.adapter.repo.workshop_repo import WorkshopRepo
 
from internal.api.material_type import MaterialType
from internal.api.product_type import ProductType
from internal.api.product_workshops import ProductWorkshops
from internal.api.products import Products
from internal.api.workshop import Workshop


def get_apps_router(conn, cursor) -> APIRouter:
    
    mtr = MaterialTypeRepo(conn, cursor)
    material_type = MaterialType(mtr).get_router()

    ptr = ProductTypeRepo(conn, cursor)
    product_type = ProductType(ptr).get_router()

    pwr = ProductWorkshopsRepo(conn, cursor)
    product_workshops = ProductWorkshops(pwr).get_router()

    pr = ProductsRepo(conn, cursor)
    products = Products(pr).get_router()

    wr = WorkshopRepo(conn, cursor)
    workshop = Workshop(wr).get_router()

    router = APIRouter()
    router.include_router(material_type, prefix="/material_type", tags=["material_type"])
    router.include_router(product_type, prefix="/product_type", tags=["product_type"])
    router.include_router(product_workshops, prefix="/product_workshops", tags=["product_workshops"])
    router.include_router(products, prefix="/products", tags=["products"])
    router.include_router(workshop, prefix="/workshop", tags=["workshop"])

    return router
