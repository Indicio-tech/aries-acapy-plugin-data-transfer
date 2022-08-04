"""Test data-transfer protocol."""
import pytest
from aries_cloudagent.connections.models.conn_record import ConnRecord
from aries_cloudagent.messaging.decorators.attach_decorator import (
    AttachDecorator,
    AttachDecoratorData,
)
from aries_cloudagent.messaging.request_context import RequestContext
from aries_cloudagent.messaging.responder import MockResponder
from aries_cloudagent.core.event_bus import EventBus, MockEventBus

from acapy_plugin_data_transfer.v0_1.data_transfer import (
    ProvideData,
    ProvideDataHandler,
)

TEST_CONN_ID = "conn-id"
TEST_DATA = AttachDecorator(
    description="test data attachment", data=AttachDecoratorData(json_={"test": "data"})
)


@pytest.fixture
def event_bus():
    """Fixture for eventn bus."""
    yield MockEventBus()


@pytest.fixture
def context(event_bus):
    """Fixture for context used in tests."""
    context = RequestContext.test_context()
    context.profile.context.injector.bind_instance(EventBus, event_bus)
    context.message = ProvideData(goal_code="test_goal", data=[TEST_DATA])
    context.connection_record = ConnRecord(connection_id=TEST_CONN_ID)
    context.connection_ready = True
    yield context


@pytest.mark.asyncio
async def test_provide_data_handler(context, event_bus: MockEventBus):
    """Test provide data handler."""
    handler, responder = ProvideDataHandler(), MockResponder()
    await handler.handle(context, responder)
    assert len(event_bus.events) == 1
    profile, event = event_bus.events[0]
    topic, payload = event.topic, event.payload
    assert topic == "acapy::webhook::data-transfer/test_goal"
    assert payload == {"connection_id": TEST_CONN_ID, "data": [TEST_DATA.serialize()]}
