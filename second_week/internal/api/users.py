from fastapi import APIRouter, HTTPException

from second_week.internal.adapter.repo.data_comments_repo import ProductWorkshopsRepo

class ProductWorkshops:
    def __init__(self, repo: ProductWorkshopsRepo):
        self.repo = repo

        self.router = APIRouter()

        self.router.post("/create", status_code=200)(self.create)
        self.router.get("/get", status_code=200)(self.get)
        self.router.get("/get/list", status_code=200)(self.get_list)
        self.router.delete("/delete", status_code=200)(self.delete)

    async def create(self, material_type: str, raw_material_loss_percentage: str):
        return self.repo.create(material_type, raw_material_loss_percentage)

    async def get(self, id):
        if self.repo.check(id):
            return self.repo.get(id)
        
        raise HTTPException(status_code=400, detail="does not exist")

    async def get_list(self):
        return self.repo.get_list()

    async def delete(self, id):
        if self.repo.check(id):
            return self.repo.delete(id)
        raise HTTPException(status_code=400, detail="does not exist")

    def get_router(self):
        return self.router