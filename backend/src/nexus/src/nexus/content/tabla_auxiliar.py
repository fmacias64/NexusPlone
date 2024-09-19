from plone import schema
from zope import schema as sche
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
from z3c.relationfield.schema import RelationChoice
from plone.autoform import directives


class ITablaAuxiliar(model.Schema):
    """Dexterity-Schema for FPN1"""

    consulta_ai = schema.Text(
        title="Consulta AI",
        description="texto que producira la consulta via AI",
        required=False,
    )
    # datasource = sche.Choice(
    #     title="Datasource",
    #     description="Dataset o Base de datos donde se basara la consulta",
    #     vocabulary="my_vocabularies_MyContentVocabulary",
    #     required=True
    # )

    datasource = RelationChoice(
        title="Datasource",
        description="Dataset o Base de datos donde se basara la consulta",
        vocabulary="data_base_dashboard_vocabulary",

        required=False
    )
    directives.widget(
        "datasource",
        frontendOptions={
            "widget": "select",
        }),
    query_mysql = schema.Text(
        title="Query Mysql",
        description="""Query que se ejecuta temporalmente 
        y guarda un resultado""",
        required=False,
    )
    base_de_datos = schema.TextLine(
        title="Base de Datos",
        description="Base de datos a la que pertenece la tabla",
        required=False,
    )
    trigger = schema.Text(
        title="Trigger",
        description="En que circunstancias debe ser usada esta consulta",
        required=False,
    )
    schedule  = schema.Choice(
        title=u'Horario de ejecucion',
        values=[u'Diario', u'Semanal', u'Mensual',u'Por hora', u'Manual'],
        required=True,
        )

    codigo_python = schema.Text(
        title="Codigo Python",
        description="Codigo Python que genera json con los resultados deseados",
        required=False,
    )

@implementer(ITablaAuxiliar)
class TablaAuxiliar(Container):
    """TablaAuxiliar instance class"""
