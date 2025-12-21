from dataclasses import dataclass

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
