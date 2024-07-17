"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "nexus"

_ = MessageFactory("nexus")

logger = logging.getLogger("nexus")
