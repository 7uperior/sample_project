import pytest

from app.domain.models import Item


@pytest.fixture()  # not for this simple test, but for future extenttion of test codebase
def item_fixture():
	"""Fixture for creating an item model instance."""
	return Item(id=1, name='Test Item', description='A test item.')


def test_item_model(item_fixture):
	item = item_fixture
	assert item.id == 1
	assert item.name == 'Test Item'
	assert item.description == 'A test item.'
