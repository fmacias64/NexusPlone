from plone import schema
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

class IDashboard(model.Schema):
    """Dexterity-Schema for Talks"""
    id_dashboard =schema.Int(
        title="Id Dashboard",
        required=False,
        description="El id correspondiente al Dashboard",
    )

    objetivo =schema.Text(
        title="Objetivo del Dashboard",
        required=False,
        description="El objetivo del Dashboard",
    )


    comentario =schema.Text(
        title="Comentario sobre Dashboard",
        required=False,
        description="comentarios del Dashboard",
    )

    
    charts = schema.TextLine(
        title="Charts",
        description="Charts presentes en el Dashboard",
        required=False,
    )

 
@implementer(IDashboard)
class Dashboard(Container):
    """Dashboard instance class"""