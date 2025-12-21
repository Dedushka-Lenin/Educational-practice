import toml

from internal.dimain import config

def Get(path: str) -> config.Config:
    config_dict = toml.load(path)
    config_obj = config.Config(
        database=config.DatabaseConfig(**config_dict['database']),
        api=config.APIConfig(**config_dict['app'])
    )

    return config_obj