from plone import schema
from plone.dexterity.content import Container
from plone.schema.jsonfield import JSONField
from plone.supermodel import model
from zope.interface import implementer

class IPuntoDePresentacion(model.Schema):
    """Dexterity-Schema for Punto de Presentacion"""
    explicacion = schema.TextLine(
        title="Explicación",
        description="Texto que se convertirá en el voice off",
        required=False,
    )

    instruccion_ai = schema.TextLine(
        title="Instrucción AI",
        description="Instrucción para realizar en un determinado chart o solo con explicación",
        required=False,
    )

    instruccion_json = JSONField(
        title="Instrucción JSON",
        description="Campo actualizado por la IA con las instrucciones correspondientes",
        required=False,
    )

    instruccion_especifica = schema.TextLine(
        title="Instrucción Específica",
        description="Si no se usa el campo que instruye a la IA para generar instrucción.",
        required=False,
    )

    chart_id = schema.Int(
        title="Chart ID",
        description="Solo si se escogió instrucción específica",
        required=False,
    )

    filtro_ = schema.TextLine(
        title="Filtro",
        description="Solo si la instrucción específica requiere un filtro",
        required=False,
    )

    user_id = schema.Int(
        title="User ID",
        description="Usuario provisional, se cambiará al ajustar KeyCloak. Siempre vale 1.",
        required=False,
        max=1,
        min=1,
    )

@implementer(IPuntoDePresentacion)
class PuntoDePresentacion(Container):
    """Punto de Presentacion instance class"""
