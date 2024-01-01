import pytest
from django.db import IntegrityError

@pytest.mark.test_conversation_db
def test_conversation_db_conversation_insert_data(db, conversation_factory):
    new_conversation = conversation_factory.create()

    fields = ["item", "members", "created_by", "created_at", "modified_at"]
    for field in fields:
        assert getattr(new_conversation, field) is not None


@pytest.mark.test_conversation_db
@pytest.mark.parametrize(
    "content",
    [
        ("This is the content test 1"),
        ("This is the content test 2"),
        ("This is the content test 3"),
    ]
)
def test_conversation_db_conversation_message_insert_data(db, conversation_message_factory, content):
    new_conversation_message = conversation_message_factory.create(content=content)

    assert new_conversation_message.conversation is not None
    assert new_conversation_message.created_by is not None
    assert new_conversation_message.created_at is not None
    assert new_conversation_message.content == content