from plone import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.autoform import directives
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.app.z3cform.widget import SelectFieldWidget
import zope.schema  

class IFPN1(model.Schema):
    """Dexterity-Schema for FPN1"""
    id_dashboard =schema.Int(
        title="Id Dashboard",
        required=False,
        description="El id correspondiente al Dashboard",
    )

    system_ai = schema.Text(
        title="Role System",
        description="""Define las especificaciones técnicas del modelo, como el tipo de modelo GPT-4 y cualquier configuración especial como longitud máxima de respuesta o tokens específicos.""",
        required=False,
    )

    role_ai = schema.Text(
        title="Role User",
        description="""Especifica el comportamiento esperado o la función del modelo dentro de la interacción, como asistente de marketing, generador de código, o asesor educativo.""",
        required=False,
    )

    tipo_de_prompt = schema.Choice(
        title="Tipo de Prompt",
        description="""Nivel de generalizacion / especializacion del prompt""",
        values=[u'Formular', u'Consolidar', u'Salida'],
        required=False,
    )

    modelo = schema.Choice(
        title=u"Modelo a utilizar",
        description=u"Selecciona el modelo de OpenAI que se empleará para aplicar el prompt. Cada modelo tiene características y capacidades diferentes adecuadas para distintos tipos de tareas.",
        values=[u'gpt-4o',  u'gpt-4', u'gpt-3.5-turbo', u'gpt-4o-mini',u'gpt-4-urbo'],
        required=False,
    )

    prioridad = schema.Choice(
        title=u"Prioridad del prompt",
        description=u"Prioridad del prompt, 1 es el mas prioritario",
        values=[u'1',  u'2', u'3', u'4',u'5'],
        required=False,
    )

    max_length = schema.Int(
        title="Max Tokens",
        description="""Define la longitud máxima de las respuestas generadas por el modelo. Este parámetro es útil para controlar la extensión de los textos producidos y asegurar que se adecuen a los límites deseados.""",
        required=False,
        default=150
    )


    temperature = schema.Float(
          title="Temperatura",
          description="""Define la temperatura que se usara para resolver el prompt""",
          required=False,
          default=0.3
      )

    
    trigger = schema.TextLine(
        title="Trigger",
        description="""Que activa este auxiliar""",
        required=False,
    )
    

    prompts_asociados = RelationList(
        title="Prompts Relacionados",
        description="Prompts asociados que se ejecutan incondicionalmente",
        value_type=RelationChoice(
            vocabulary="prompts_asociados_vocabulary",
        ),
        required=False
    )
   
    directives.widget(
        "prompts_asociados",
        frontendOptions={
            "widget": "select",
        },
    )

    servicio_asignado = RelationChoice(
        title="Servicio Asignado",
        description="Si el prompt requiere un servicio",
        vocabulary="servicio_vocabulary",

        required=False
    )
    directives.widget(
        "servicio_asignado",
        frontendOptions={
            "widget": "select",
        })

    tablas_auxiliares = RelationList(
        title="Tablas auxiliares",
        description="Seleccion de tablas auxiliares para este FPN2",
        value_type=RelationChoice(
            vocabulary="tabla_auxiliar_vocabulary",
        ),
        required=False
    )
   
    directives.widget(
        "tablas_auxiliares",
        frontendOptions={
            "widget": "select",
        },
    )

@implementer(IFPN1)
class FPN1(Container):
    """FPN1 instance class"""
