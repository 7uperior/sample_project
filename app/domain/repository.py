from typing import List, Protocol

from app.domain.schemas import Item, ItemCreate


class ItemRepository(Protocol):
	async def get_all_items(self) -> List[Item]:
		pass

	async def add_item(self, item: ItemCreate) -> Item:
		pass
