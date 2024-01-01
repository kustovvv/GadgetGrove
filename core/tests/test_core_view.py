import pytest
from django.urls import reverse

from item.models import Item

@pytest.mark.test_core_view
def test_core_view_frontpage(db, client, item_factory):
    items = [item_factory.create() for _ in range(4)]
    url = reverse('frontpage')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context['items']) == len(items)
    assert len(response.context['categories']) == len(items)
    

