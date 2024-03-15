import pytest

from app.domain.models import Item
from app.domain.repository import ItemRepository
from app.domain.schemas import ItemCreate


class MockItemRepository(ItemRepository):
	async def get_all_items(self) -> list[Item]:
		return [Item(id=1, name='Mock Item', description='A mock item.')]

	async def add_item(self, item: ItemCreate) -> Item:
		return Item(id=2, **item.dict())


# Directly instantiate MockItemRepository in each test function
@pytest.mark.asyncio()
async def test_add_item():
	mock_repo = MockItemRepository()
	item_create = ItemCreate(name='Test Item', description='A test item.')
	item = await mock_repo.add_item(item_create)

	assert item.id == 2  # Assuming the mock_repo assigns a new ID
	assert item.name == 'Test Item'
	assert item.description == 'A test item.'


@pytest.mark.asyncio()
async def test_get_all_items():
	mock_repo = MockItemRepository()
	items = await mock_repo.get_all_items()

	assert len(items) > 0
	assert items[0].name == 'Mock Item'
	assert items[0].description == 'A mock item.'
