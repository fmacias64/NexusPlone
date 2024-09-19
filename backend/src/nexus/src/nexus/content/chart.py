from plone import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer

class IChart(model.Schema):
    """Dexterity-Schema for Chart"""

    id_chart = schema.Int(
        title="Id Chart",
        description="Identificador del Chart",
        required=False,
    )

    campo_filtrado = schema.TextLine(
        title="Campo Filtro",
        description="Campo principal a filtrar",
        required=False,
    )

    explicacion_campo = schema.Text(
        title="Metadata Cmpo",
        description="Explicacion a detalle del campo donde se aplica el filtro",
        required=False,
    )

    el_query = schema.Text(
        title="Query",
        description="Query que produce la visualización",
        required=False,
    )

    dd_query = schema.Text(
        title="Diccionario de datos Query",
        description="Sentido a los campos de la tabla del query",
        required=False,
    )

    finalidad_relaciones = schema.Text(
        title="Relaciones del chart",
        description="Como se relaciona con otros charts",
        required=False,
    )

    objetivo = schema.Text(
        title="Objetivo",
        description="Cuál es la razón del chart en el dashboard",
        required=False,
    )
     
    filtros_posibles = schema.Text(
        title="Filtros Posibles",
        description="Lista con los filtros posibles para este chart",
        required=False,
    )

    dashboard_asignado = schema.Int(
        title="Dashboard Asignado",
        description="Dashboard al cual está asignado",
        required=False,
    )


    viz_type = schema.TextLine(
        title="Tipo de Visualización",
        description="Tipo de visualización usada",
        required=False,
    )



    id_dataset = schema.Int(
        title="Id Dataset",
        description="Id del dataset en Superset",
        required=False,
    )

@implementer(IChart)
class Chart(Container):
    """Chart instance class"""
