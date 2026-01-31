from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from internal.adapter.token.token import TokenManager
from internal.adapter.repo.requests_repo import RequestsRepo

from internal.domain.exceptions import ApiError, InsufficientRights

class Requests:
    def __init__(self, repo: RequestsRepo, token: TokenManager):
        self.repo = repo
        self.token = token

        self.router = APIRouter()

        self.router.post("/create", status_code=200)(self.create)
        self.router.get("/get", status_code=200)(self.get)
        self.router.get("/get/list", status_code=200)(self.get_list)
        self.router.delete("/delete", status_code=200)(self.delete)

    async def create(self, startDate: str, homeTechType: str, homeTechModel: str, problemDescryption: str, requestStatus: str, completionDate: str, repairParts: str, clientID: int, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        try:
            user_id = self.token.get_id(credentials) 
            user_inf = self.repo.get(user_id)

            if user_inf["type"] != "Менеджер" or user_inf["type"] != "Специалист" or user_inf["type"] != "Оператор":
                raise InsufficientRights()

            return self.repo.create(startDate, homeTechType, homeTechModel, problemDescryption, requestStatus, completionDate, repairParts, user_id, clientID)
        
        except ApiError as e:
            data_error = e.get_error()
            raise HTTPException(status_code=data_error["status_code"], detail=data_error["detail"])

    async def get(self, id, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        try:
            user_id = self.token.get_id(credentials) 
            user_inf = self.repo.get(user_id)

            if user_inf["type"] != "Менеджер" or user_inf["type"] != "Специалист" or user_inf["type"] != "Оператор":
                raise InsufficientRights()

            if self.repo.check(id):
                return self.repo.get(id)
            
            raise HTTPException(status_code=400, detail="does not exist")
        
        except ApiError as e:
            data_error = e.get_error()
            raise HTTPException(status_code=data_error["status_code"], detail=data_error["detail"])

    async def get_list(self, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        try:
            user_id = self.token.get_id(credentials) 
            user_inf = self.repo.get(user_id)

            if user_inf["type"] != "Менеджер" or user_inf["type"] != "Специалист" or user_inf["type"] != "Оператор":
                raise InsufficientRights() 

            return self.repo.get_list()
        
        except ApiError as e:
            data_error = e.get_error()
            raise HTTPException(status_code=data_error["status_code"], detail=data_error["detail"])

    async def delete(self, id, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        try:
            user_id = self.token.get_id(credentials) 
            user_inf = self.repo.get(user_id)

            if user_inf["type"] != "Менеджер" or user_inf["type"] != "Специалист" or user_inf["type"] != "Оператор":
                raise InsufficientRights() 

            if self.repo.check(id):
                return self.repo.delete(id)
            raise HTTPException(status_code=400, detail="does not exist")
    
        except ApiError as e:
            data_error = e.get_error()
            raise HTTPException(status_code=data_error["status_code"], detail=data_error["detail"])

    def get_router(self):
        return self.router
