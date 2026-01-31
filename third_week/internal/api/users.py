from enum import Enum

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from fastapi import APIRouter, HTTPException

from internal.domain.exceptions import ApiError, UserNotFound

from internal.adapter.token.token import TokenManager
from internal.adapter.repo.users_repo import UsersRepo

class UserType(str, Enum):
    Manager = 'Менеджер'
    Specialist = 'Специалист'
    Operator = 'Оператор'
    Customer = 'Заказчик'

class Users:
    def __init__(self, repo: UsersRepo, token: TokenManager):
        self.repo = repo
        self.token = token

        self.router = APIRouter()

        self.router.post("/register", status_code=200)(self.register)
        self.router.post("/login", status_code=200)(self.login)
        self.router.post("/logout", status_code=200)(self.logout)
        self.router.get("/info", status_code=200)(self.info)

    async def register(self, fio: str, phone: int, login: str, password: str, type: UserType):
        try:
            if self.repo.check_login(login):
                raise HTTPException(status_code=400, detail="A user with this name already exists")

            self.repo.create(fio, phone, login, password, type)
            return {"message": "User successfully created"}
                
        except ApiError as e:
            data_error = e.get_error()
            raise HTTPException(status_code=data_error["status_code"], detail=data_error["detail"])

    async def login(self, login, password):
        try:
            user_inf = self.repo.get_for_login(login)

            if not user_inf or not user_inf["password"] == password:
                raise UserNotFound

            token = self.token.create(user_inf["id"])
            return {"access_token": token}
            
        except ApiError as e:
            data_error = e.get_error()
            raise HTTPException(status_code=data_error["status_code"], detail=data_error["detail"])

    async def logout(self, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        try:
            token = credentials.credentials
            self.token.disability(token)

            return {"message": "The token is invalidated"}
            
        except ApiError as e:
            data_error = e.get_error()
            raise HTTPException(status_code=data_error["status_code"], detail=data_error["detail"])

    async def info(self, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        try:
            user_id = self.token.get_id(credentials) 
            user_inf = self.repo.get(user_id)

            return {"message": "The token is valid", "login": user_inf["login"]}
            
        except ApiError as e:
            data_error = e.get_error()
            raise HTTPException(status_code=data_error["status_code"], detail=data_error["detail"])

    def get_router(self):
        return self.router