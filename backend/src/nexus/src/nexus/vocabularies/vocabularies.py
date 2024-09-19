from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone import api


@provider(IVocabularyFactory)
def my_content_vocabulary(context=None):
    if context is not None:
        # Obtiene la ruta física del contexto y excluye el último elemento
        path_elements = context.getPhysicalPath()[:-1]  # Excluye el último elemento
        
        # Obtiene el catálogo y realiza la consulta
        catalog = api.portal.get_tool(name='portal_catalog')
        query = {"portal_type": ["data_base", "dataset"], "review_state": "private"}
        results = catalog.searchResults(query)
        #path_elements=('', 'Plone', 'control', 'proyectos')
        #print(path_elements)
        # Filtra y crea los términos basándose en el path modificado
        terms = []
        for item in results:
            item_path_elements = item.getPath().split('/')[:-1]  # Excluye el último elemento del path del ítem
            if all(elem in item_path_elements for elem in path_elements):
                terms.append(SimpleTerm(value=item.getPath(), token=item.getPath(), title=item.Title))
        
        # Imprime el path para verificar
        print(context.getPhysicalPath())  
        return SimpleVocabulary(terms)

    # Si el contexto es None, devuelve un vocabulario vacío
    return SimpleVocabulary([])
# def my_content_vocabulary(context=None):
#     catalog = api.portal.get_tool(name='portal_catalog')
#     query = {"portal_type":["data_base","dataset"],"review_state": "private"}  # Cambia 'MyType' al tipo que necesitas
#     results = catalog.searchResults(query)
#     terms = [
#         SimpleTerm(value=item.getPath(), token=item.getPath(), title=item.Title)
#         for item in results
#     ]
#     print(context.getPhysicalPath())
#     return SimpleVocabulary(terms)


@provider(IVocabularyFactory)
def DocumentVocabularyFactory(context=None):
    return StaticCatalogVocabulary(
        {
            "portal_type": ["Document", "News Item"],
            "sort_on": "sortable_title",
        }
    )


@provider(IVocabularyFactory)
def TablaAuxiliarVocabulary(context=None):
    SCV = StaticCatalogVocabulary(
        {
            "portal_type": ["tabla_auxiliar"],
            "review_state": "private",
            #"sort_on": "sortable_title",
            "path":"/Plone/control/"
        }
    )
    #print(dir(SCV))
    return SCV


@provider(IVocabularyFactory)
def PromptAsociadoVocabulary(context=None):
    name="prompts_asociados_vocabulary"
    SCV = StaticCatalogVocabulary(
        {
            "portal_type": ["fpn1"],
            "review_state": "private",
            #"sort_on": "sortable_title",
            "path":"/Plone/control/"
        }
    )
    #print(dir(SCV))
    return SCV

@provider(IVocabularyFactory)
def DataSourceVocabulary(context=None):
    name="data_base_dashboard_vocabulary"
    SCV = StaticCatalogVocabulary(
        {
            "portal_type": ["data_base","dataset"],
            "review_state": "private",
            #"sort_on": "sortable_title",
            "path": '/Plone/control/'
        }
    )
   
    return SCV


@provider(IVocabularyFactory)
def ServicioVocabulary(context=None):
    name="servicio_vocabulary"
    SCV = StaticCatalogVocabulary(
        {
            "portal_type": ["servicio"],
            "review_state": "private",
            #"sort_on": "sortable_title",
            "path": '/Plone/control/'
        }
    )
   
    return SCV


@provider(IVocabularyFactory)
def AudiencesVocabulary(context):
    name = "ploneconf.audiences"
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    return SimpleVocabulary.fromItems(
        [[item["token"], item["token"], item["titles"][lang]] for item in items]
    )