from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    MODE: Literal['DEV', 'TEST', 'PROD'] = 'DEV'

    SECRET_KEY: str
    ALGORITHM: str

    ACCESS_TOKEN_EXP_MINUTES: int = 15

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DB_URI(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str

    @property
    def TEST_DB_URI(self):
        return (
            f'postgresql+asyncpg://{self.TEST_DB_USER}:'
            f'{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:'
            f'{self.TEST_DB_PORT}/{self.TEST_DB_NAME}'
        )

    REDIS_HOST: str
    REDIS_PORT: int
    CACHE_TTL: int = 180

    @property
    def REDIS_URL(self):
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}'


settings = Settings()
