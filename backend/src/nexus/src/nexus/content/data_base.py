from plone import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer

class IDatabase(model.Schema):
    """Dexterity-Schema for Chart"""

    id_database = schema.Int(
        title="Id Database",
        description="Identificador de la Base de Datos",
        required=False,
    )

    descripcion_er = schema.Text(
        title="Descripcion ER",
        description="Entidad Realcion en reglas de produccion",
        required=False,
    )

@implementer(IDatabase)
class Database(Container):
    """Database instance class"""
