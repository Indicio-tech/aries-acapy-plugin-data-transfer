"""Data Transfer Plugin."""
from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.core.protocol_registry import ProtocolRegistry

from .data_transfer import MESSAGE_TYPES


async def setup(
    context: InjectionContext, protocol_registry: ProtocolRegistry = None
):
    """Data Transfer protocol plugin setup."""
    if not protocol_registry:
        protocol_registry = await context.inject(ProtocolRegistry)
    protocol_registry.register_message_types(MESSAGE_TYPES)
