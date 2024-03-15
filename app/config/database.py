from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings
from app.domain.models import Base  # Ensure your ORM base is imported here

engine = create_async_engine(settings.database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


async def init_db():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
