from plone import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer

class IServicio(model.Schema):
    """Dexterity-Schema for Chart"""

    api_key = schema.TextLine(
        title="API-KEY",
        description="Api key dada por el servicio",
        required=False,
    )

    enlace_del_servicio = schema.URI(
        title="Direccion del servicio (URL)",
        description="El enlace del REST-API donde hacer llamados ",
        required=False,
    )


@implementer(IServicio)
class Servicio(Container):
    """Database instance class"""
