# app/config/settings.py
from pydantic import BaseSettings


class Settings(BaseSettings):
	postgres_user: str
	postgres_password: str
	postgres_db: str
	database_host: str

	@property
	def database_url(self) -> str:
		return f'postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.database_host}/{self.postgres_db}'

	class Config:
		env_file = '.env'


settings = Settings()


def get_settings() -> Settings:
	return settings
