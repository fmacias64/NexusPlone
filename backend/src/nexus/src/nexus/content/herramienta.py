from plone import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer

class IHerramienta(model.Schema):
    """Dexterity-Schema for Chart"""

    herramienta = schema.TextLine(
        title="Nombre herramienta con parametros",
        description="Nombre de funcion o endpoint de herramienta",
        required=False,
    )

    invocacion = schema.Text(
        title="Detalles e instrucciones de uso",
        description="Instrucciones requeridas para usar herramienta ",
        required=False,
    )


@implementer(IHerramienta)
class Herramienta(Container):
    """Database instance class"""
