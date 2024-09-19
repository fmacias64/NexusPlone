from plone import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer

class IDataset(model.Schema):
    """Dexterity-Schema for Dataset"""
    id_dataset = schema.Int(
        title="Id Dataset",
        description="Id del dataset en Superset",
        required=False,
    )

    definicion = schema.Text(
        title="Definición",
        description="SQL Create",
        required=False,
    )

    data_dictionary = schema.Text(
        title="DD",
        description="Diccionario de datos del Dataset",
        required=False,
    )

    dd_automatico = schema.Text(
        title="DD Automático",
        description="Diccionario de datos inferido por la IA",
        required=False,
    )

    tabla = schema.TextLine(
        title="Tabla",
        description="Nombre de la tabla en la que está basado",
        required=False,
    )

    base_de_datos = schema.TextLine(
        title="Base de Datos",
        description="Base de datos a la que pertenece la tabla",
        required=False,
    )

    tabla_virtual = schema.Text(
        title="Tabla Virtual",
        description="Query en el que se basa el dataset",
        required=False,
    )
    changed = schema.TextLine(
        title="Ultima vez cambiado",
        description="Fecha y hora de ultimo cmabio",
        required=False,
    )

@implementer(IDataset)
class Dataset(Container):
    """Dataset instance class"""
