from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repository.sql_repository import SQLItemRepository
from app.config.database import SessionLocal
from app.domain.schemas import Item, ItemCreate

router = APIRouter()


# Dependency to get a session
async def get_session() -> AsyncSession:
	async with SessionLocal() as session:
		yield session


# Adjusted dependency to provide a repository with a session
async def get_item_repository(session: AsyncSession = Depends(get_session)) -> SQLItemRepository:
	return SQLItemRepository(session)


@router.get('/items/', response_model=list[Item])
async def read_items(repository: SQLItemRepository = Depends(get_item_repository)):
	items = await repository.get_all_items()
	return items


@router.post('/items/', response_model=Item)
async def add_item(item: ItemCreate, repository: SQLItemRepository = Depends(get_item_repository)):
	new_item = await repository.add_item(item)
	return new_item
