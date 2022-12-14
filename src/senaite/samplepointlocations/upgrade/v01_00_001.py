# -*- coding: utf-8 -*-

from bika.lims import api
from senaite.core.upgrade import upgradestep
from senaite.samplepointlocations import PRODUCT_NAME
from senaite.samplepointlocations import logger

version = "1.0.1"


@upgradestep(PRODUCT_NAME, version)
def upgrade(tool):
    portal = tool.aq_inner.aq_parent
    change_action_title(portal)
    logger.info("{0} upgraded to version {1}".format(PRODUCT_NAME, version))
    return True


def change_action_title(portal):
    pt = api.get_tool("portal_types", context=portal)
    fti = pt.get("Client")
    actions = fti.listActions()
    for action in actions:
        if action.id == "samplepointlocations":
            action.title = "Sample Point Locations"
            logger.info("Changed action title to Sample Point Location")
