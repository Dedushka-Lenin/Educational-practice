from fastapi import APIRouter

from internal.adapter.repo.products_repo import ProductsRepo

class Products:
    def __init__(self, repo: ProductsRepo):
        self.repo = repo

        self.router = APIRouter()

        self.router.post("/create", status_code=200)(self.create)
        self.router.get("/get", status_code=200)(self.get)
        self.router.get("/get/list", status_code=200)(self.get_list)
        self.router.delete("/delete", status_code=200)(self.delete)

    async def create(self, product_type: str, product_name: str, part_number: str, minimum_partner_cost: str, primary_material: str):
        return self.repo.create(product_type, product_name, part_number, minimum_partner_cost, primary_material)

    async def get(self, id):
        return self.repo.get(id)

    async def get_list(self):
        return self.repo.get_list()

    async def delete(self, id):
        return self.repo.delete(id)

    def get_router(self):
        return self.router
