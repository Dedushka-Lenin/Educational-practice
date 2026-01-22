from fastapi import APIRouter

from internal.adapter.repo.comments_repo import CommentsRepo
from internal.adapter.repo.requests_repo import RequestsRepo
from internal.adapter.repo.token_repo import TokenRepo
from internal.adapter.repo.users_repo import UsersRepo
 
from internal.api.comments import Comments
from internal.api.requests import Requests
from internal.api.users import Users

from internal.adapter.token.token import TokenManager
from internal.adapter.config.config import TokenConfig  


def get_apps_router(conn, cursor, token_conf: TokenConfig) -> APIRouter:

    token_repo = TokenRepo(conn, cursor)
    token_manager = TokenManager(token_conf, token_repo)
    
    requests_repo = RequestsRepo(conn, cursor)
    requests = Requests(requests_repo, token_manager).get_router()

    comments_repo = CommentsRepo(conn, cursor)
    comments = Comments(comments_repo, requests_repo, token_manager).get_router()

    users_repo = UsersRepo(conn, cursor)
    users = Users(users_repo, token_manager).get_router()

    router = APIRouter()
    router.include_router(comments, prefix="/comments", tags=["comments"])
    router.include_router(requests, prefix="/requests", tags=["requests"])
    router.include_router(users, prefix="/users", tags=["users"])

    return router
