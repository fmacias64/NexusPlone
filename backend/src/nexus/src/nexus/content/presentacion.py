from plone import schema
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer

class IPresentacion(model.Schema):
    """Dexterity-Schema for Presentacion"""
    dashboard_id = schema.Int(
        title="Dashboard",
        description="Identificador del Dashboard",
    )

    details = RichText(
        title="Details",
        description="Detalles a ver en código",
        required=False,
    )

@implementer(IPresentacion)
class Presentacion(Container):
    """Presentacion instance class"""
