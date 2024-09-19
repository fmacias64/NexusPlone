from plone import schema
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from plone.autoform import directives
from z3c.form.browser.radio import RadioFieldWidget

class IPolitica(model.Schema):
    """Dexterity-Schema for Chart"""
    expect = schema.Text(
        title="Expect",
        description="A que tipo de pregunta reaccionar",
        required=False,
    )
    directives.widget(obligatoria=RadioFieldWidget)
    obligatoria = schema.Bool(
        title="Política obligatoria",
        description="Especifica si la politica debe aplicarse de forma obligatoria",
        required=False,
    )

    activacion = schema.Text(
        title="Activación",
        description="Temas o palabras clave que pueden activar la pol&iacute;tica o comentario",
        required=False,
    )

@implementer(IPolitica)
class Politica(Container):
    """Politica respuesta instance class"""
