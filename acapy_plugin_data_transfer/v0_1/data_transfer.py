"""Define messages and handlers for data-transfer protocol."""
import logging
from typing import Sequence

from aries_cloudagent.messaging.agent_message import (
    AgentMessage, AgentMessageSchema
)
from aries_cloudagent.messaging.base_handler import BaseHandler, BaseResponder
from aries_cloudagent.messaging.decorators.attach_decorator import (
    AttachDecorator, AttachDecoratorSchema
)
from aries_cloudagent.messaging.request_context import RequestContext
from marshmallow import fields

from .message_types import PROVIDE_DATA

LOGGER = logging.getLogger(__name__)


class ProvideData(AgentMessage):
    """Class representing a provide data message."""

    class Meta:
        """ProvideData metadata."""

        handler_class = "ProvideDataHandler"
        schema_class = "ProvideDataSchema"
        message_type = PROVIDE_DATA

    def __init__(
        self,
        _id: str = None,
        *,
        goal_code: str = None,
        data: Sequence[AttachDecorator] = None,
        **kwargs,
    ):
        super().__init__(_id=_id, **kwargs)
        self.goal_code = goal_code
        self.data = data


class ProvideDataSchema(AgentMessageSchema):
    """ProvideData schema."""

    class Meta:
        """ProvideData schema metadata."""

        model_class = ProvideData
        # unknown = EXCLUDE

    goal_code = fields.Str(required=True)
    data = fields.Nested(
        AttachDecoratorSchema, required=True, many=True, data_key="data~attach"
    )


class ProvideDataHandler(BaseHandler):
    """Handler for provide data message."""

    WEBHOOK_TOPIC = "data-transfer"

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Handle provide data message."""
        LOGGER.debug(
            "Received data through provide-data message: %s", context.message
        )
        assert isinstance(context.message, ProvideData)

        data: Sequence[AttachDecorator] = context.message.data

        await responder.send_webhook(
            topic=f"{self.WEBHOOK_TOPIC}/{context.message.goal_code}",
            payload={
                "connection_id": context.connection_record.connection_id,
                "data": list(map(lambda datum: datum.serialize(), data))
            },
        )
