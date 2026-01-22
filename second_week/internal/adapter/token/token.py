import time
from authlib.jose import jwt, JoseError

from internal.adapter.config.config import TokenConfig
from internal.adapter.repo.token_repo import TokenRepo
from internal.domain.exceptions import InvalidToken


class TokenManager:
    def __init__(self, conf: TokenConfig, repo: TokenRepo):
        self.repo = repo
        self.conf = conf

    def create(self, user_id: str) -> str:
        header = {"alg": self.conf.algorithm}
        payload = {
            "sub": user_id,
            "exp": int(time.time()) + self.conf.token_expire_seconds,
        }
        token_bytes = jwt.encode(header, payload, self.conf.secret_key)
        token = token_bytes.decode("utf-8")

        self.repo.create(token=token, user_id=user_id)
        return token

    def check(self, token: str):
        # Вначале проверяем наличие токена в базе
        if not self.repo.check(token):
            raise InvalidToken()

        try:
            claims = jwt.decode(token, self.conf.secret_key)
            claims.validate()
            return claims
        except JoseError:
            self.disability(token)
            raise InvalidToken()

    def disability(self, token: str):
        try:
            self.check(token)
        except InvalidToken:
            pass
        finally:
            self.repo.delete(token)

    def get_id(self, credentials) -> str:
        token = credentials.credentials
        claims = self.check(token)
        user_id = claims.get("sub")
        if not user_id:
            raise InvalidToken()
        return user_id