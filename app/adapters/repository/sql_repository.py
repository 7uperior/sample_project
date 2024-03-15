from sqlalchemy.future import select

from app.config.database import AsyncSession
from app.domain.models import Item as ORMItem
from app.domain.repository import ItemRepository
from app.domain.schemas import Item, ItemCreate


class SQLItemRepository(ItemRepository):
	def __init__(self, session: AsyncSession):
		self.session = session

	async def get_all_items(self) -> list[Item]:
		result = await self.session.execute(select(ORMItem))
		items = result.scalars().all()
		return [Item.from_orm(item) for item in items]

	async def add_item(self, item: ItemCreate) -> Item:
		new_item = ORMItem(name=item.name, description=item.description)
		self.session.add(new_item)
		await self.session.commit()
		await self.session.refresh(new_item)
		return Item.from_orm(new_item)
