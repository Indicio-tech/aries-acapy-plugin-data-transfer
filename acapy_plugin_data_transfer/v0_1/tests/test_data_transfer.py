"""Test data-transfer protocol."""
import pytest
from aries_cloudagent.connections.models.connection_record import (
    ConnectionRecord
)
from aries_cloudagent.messaging.decorators.attach_decorator import (
    AttachDecorator, AttachDecoratorData
)
from aries_cloudagent.messaging.request_context import RequestContext
from aries_cloudagent.messaging.responder import MockResponder

from ..data_transfer import ProvideData, ProvideDataHandler

TEST_CONN_ID = "conn-id"
TEST_DATA = AttachDecorator(
    description="test data attachment",
    data=AttachDecoratorData(
        json_={"test": "data"}
    )
)


@pytest.fixture
def context():
    """Fixture for context used in tests."""
    # pylint: disable=W0621
    context = RequestContext()
    context.message = ProvideData(goal_code="test_goal", data=[TEST_DATA])
    print(context.message.serialize(as_string=True))
    context.connection_record = ConnectionRecord(connection_id=TEST_CONN_ID)
    context.connection_ready = True
    yield context


# pylint: disable=W0621


@pytest.mark.asyncio
async def test_provide_data_handler(context):
    """Test provide data handler."""
    handler, responder = ProvideDataHandler(), MockResponder()
    await handler.handle(context, responder)
    assert len(responder.webhooks) == 1
    topic, payload = responder.webhooks[0]
    assert topic == "data-transfer/test_goal"
    assert payload == {"data": [TEST_DATA]}
