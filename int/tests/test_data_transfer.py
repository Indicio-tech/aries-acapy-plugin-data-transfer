"""Test Data Transfer Plugin."""
from echo_agent.client import EchoClient
from echo_agent.models import ConnectionInfo
import pytest

TEST_DATA = {"description": "test data attachment", "data": {"json": {"test": "data"}}}


@pytest.mark.asyncio
async def test_data_transfer_webhook_emitted(
    echo: EchoClient, connection: ConnectionInfo, connection_id: str
):
    await echo.send_message(
        connection,
        {
            "@type": "https://didcomm.org/data-transfer/0.1/provide-data",
            "goal_code": "test_goal",
            "data~attach": [TEST_DATA],
        },
    )
    webhook = await echo.get_webhook(topic="topic/data-transfer/test_goal/")
    assert webhook["payload"] == {"connection_id": connection_id, "data": [TEST_DATA]}
