"""Define message types."""

PROTOCOL = "https://didcomm.org/data-transfer"
VERSION = "0.1"
BASE = "{}/{}".format(PROTOCOL, VERSION)

REQUEST_DATA = "{}/request-data".format(BASE)
PROVIDE_DATA = "{}/provide-data".format(BASE)

MESSAGE_TYPES = {
    PROVIDE_DATA: "data_transfer.ProvideData",
}
