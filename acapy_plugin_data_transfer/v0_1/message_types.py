"""Define message types."""

PROTOCOL = "https://didcomm.org/data-transfer"
VERSION = "0.1"
BASE = "{}/{}".format(PROTOCOL, VERSION)

REQUEST_DATA = "{}/request-data".format(BASE)
PROVIDE_DATA = "{}/provide-data".format(BASE)

MESSAGE_TYPES = {
    PROVIDE_DATA: "acapy_plugin_data_transfer.v0_1.data_transfer.ProvideData",
}
