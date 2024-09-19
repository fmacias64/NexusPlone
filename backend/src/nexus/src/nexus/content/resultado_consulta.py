from plone import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer

class IResultadoConsulta(model.Schema):
    """Dexterity-Schema for FPN1"""

    resultado_json = schema.Text(
        title="Resultado JSON",
        description="""Resultado en json de la consulta auxiiar """,
        required=False,
    )
    fecha_ejecucion= schema.Datetime(
        title="Fecha Ejecucion",
        description="""Fecha en la que se llevo a cabo esta consulta""",
        required=False,
    )
    query_ejecutado = schema.Text(
        title="Query Ejecutado",
        description="""Query rque origino el resultado """,
        required=False,
    )

    opinion_analista = schema.Text(
        title="Opinion Analista",
        description="""Comentarios destinados a prompt superiores """,
        required=False,
    )
    
    opinion_ia = schema.Text(
        title="Opinion IA",
        description="""Comentarios destinados a prompt superiores """,
        required=False,
    )

@implementer(IResultadoConsulta)
class ResultadoConsulta(Container):
    """ResultadoConsulta instance class"""
