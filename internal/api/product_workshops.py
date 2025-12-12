from fastapi import APIRouter

from internal.adapter.repo.product_workshops_repo import ProductWorkshopsRepo

class ProductWorkshops:
    def __init__(self, repo: ProductWorkshopsRepo):
        self.repo = repo

        self.router = APIRouter()

        self.router.post("/create", status_code=200)(self.create)
        self.router.get("/get", status_code=200)(self.get)
        self.router.get("/get/list", status_code=200)(self.get_list)
        self.router.delete("/delete", status_code=200)(self.delete)

    async def create(self, product_name: str, workshop_name: str, manufacturing_time_h: str):
        return self.repo.create(product_name, workshop_name, manufacturing_time_h)

    async def get(self, id):
        return self.repo.get(id)

    async def get_list(self):
        return self.repo.get_list()

    async def delete(self, id):
        return self.repo.delete(id)

    def get_router(self):
        return self.router
 
