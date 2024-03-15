import pytest

from app.domain.models import Item
from app.domain.repository import ItemRepository
from app.domain.schemas import ItemCreate

# Constants for mock IDs and data
MOCK_ITEM_ID = 2
MOCK_ITEM_NAME = 'Test Item'
MOCK_ITEM_DESCRIPTION = 'A test item.'


class MockItemRepository(ItemRepository):
	async def get_all_items(self) -> list[Item]:
		return [Item(id=1, name='Mock Item', description='A mock item.')]

	async def add_item(self, item: ItemCreate) -> Item:
		return Item(id=MOCK_ITEM_ID, **item.dict())


# Directly instantiate MockItemRepository in each test function
@pytest.mark.asyncio()
async def test_add_item():
	mock_repo = MockItemRepository()
	item_create = ItemCreate(name=MOCK_ITEM_NAME, description=MOCK_ITEM_DESCRIPTION)
	item = await mock_repo.add_item(item_create)

	assert item.id == MOCK_ITEM_ID
	assert item.name == MOCK_ITEM_NAME
	assert item.description == MOCK_ITEM_DESCRIPTION


@pytest.mark.asyncio()
async def test_get_all_items():
	mock_repo = MockItemRepository()
	items = await mock_repo.get_all_items()

	assert len(items) > 0
	assert items[0].name == 'Mock Item'
	assert items[0].description == 'A mock item.'
