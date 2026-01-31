import toml

from dataclasses import dataclass

@dataclass
class TokenConfig:
    secret_key: str
    algorithm: str
    token_expire_seconds: int

@dataclass
class DatabaseConfig:
    db_path: str

@dataclass
class APIConfig:
    project_name: str
    version: str
    debug: bool
    cors_allowed_origins: str

@dataclass
class Config:
    database: DatabaseConfig
    api: APIConfig
    token: TokenConfig

def Get(path: str) -> Config:
    config_dict = toml.load(path)
    config_obj = Config(
        database=DatabaseConfig(**config_dict['database']),
        api=APIConfig(**config_dict['app']),
        token=TokenConfig(**config_dict['token'])
    )

    return config_obj