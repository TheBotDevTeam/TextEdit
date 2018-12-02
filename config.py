from configlib import BaseConfig


class Config(BaseConfig):
    token: str
    prefix: str
    dbo_token: str


config = Config.get_instance()
