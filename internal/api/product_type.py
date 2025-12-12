from fastapi import APIRouter

from internal.adapter.repo.product_type_repo import ProductTypeRepo

class ProductType:
    def __init__(self, repo: ProductTypeRepo):
        self.repo = repo

        self.router = APIRouter()

        self.router.post("/create", status_code=200)(self.create)
        self.router.get("/get", status_code=200)(self.get)
        self.router.get("/get/list", status_code=200)(self.get_list)
        self.router.delete("/delete", status_code=200)(self.delete)

    async def create(self, product_type: str, product_type_coefficient: str):
        return self.repo.create(product_type, product_type_coefficient)

    async def get(self, id):
        return self.repo.get(id)

    async def get_list(self):
        return self.repo.get_list()

    async def delete(self, id):
        return self.repo.delete(id)

    def get_router(self):
        return self.router
 
