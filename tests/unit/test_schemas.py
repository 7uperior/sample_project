from app.domain.schemas import ItemCreate


def test_item_create_schema():
	item_data = {'name': 'Test Item', 'description': 'A test item description.'}
	item = ItemCreate(**item_data)

	assert item.name == 'Test Item'
	assert item.description == 'A test item description.'
