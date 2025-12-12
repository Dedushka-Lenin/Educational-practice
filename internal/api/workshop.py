from fastapi import APIRouter

from internal.adapter.repo.workshop_repo import WorkshopRepo

class Workshop:
    def __init__(self, repo: WorkshopRepo):
        self.repo = repo

        self.router = APIRouter()

        self.router.post("/create", status_code=200)(self.create)
        self.router.get("/get", status_code=200)(self.get)
        self.router.get("/get/list", status_code=200)(self.get_list)
        self.router.delete("/delete", status_code=200)(self.delete)

    async def create(self, workshop_name: str, workshop_type: str, number_people_production: str):
        return self.repo.create(workshop_name, workshop_type, number_people_production)

    async def get(self, id):
        return self.repo.get(id)

    async def get_list(self):
        return self.repo.get_list()

    async def delete(self, id):
        return self.repo.delete(id)

    def get_router(self):
        return self.router
