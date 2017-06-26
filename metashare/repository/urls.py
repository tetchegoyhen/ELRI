from django.conf.urls import patterns, url

from haystack.views import search_view_factory
from haystack.query import SearchQuerySet

from metashare.repository.forms import FacetedBrowseForm
from metashare.repository.views import MetashareFacetedSearchView

sqs = SearchQuerySet() \
  .facet("languageNameFilter") \
  .facet("resourceTypeFilter") \
  .facet("mediaTypeFilter") \
  .facet("availabilityFilter") \
  .facet("licenceFilter") \
  .facet("restrictionsOfUseFilter") \
  .facet("validatedFilter") \
  .facet("foreseenUseFilter") \
  .facet("useNlpSpecificFilter") \
  .facet("lingualityTypeFilter") \
  .facet("multilingualityTypeFilter") \
  .facet("modalityTypeFilter") \
  .facet("dataFormatFilter") \
  .facet("bestPracticesFilter") \
  .facet("domainFilter") \
  .facet("subjectFilter") \
  .facet("corpusAnnotationTypeFilter") \
  .facet("corpusAnnotationFormatFilter") \
  .facet("languageDescriptionLDTypeFilter") \
  .facet("languageDescriptionEncodingLevelFilter") \
  .facet("languageDescriptionGrammaticalPhenomenaCoverageFilter") \
  .facet("lexicalConceptualResourceLRTypeFilter") \
  .facet("lexicalConceptualResourceEncodingLevelFilter") \
  .facet("lexicalConceptualResourceLinguisticInformationFilter") \
  .facet("toolServiceToolServiceTypeFilter") \
  .facet("toolServiceToolServiceSubTypeFilter") \
  .facet("toolServiceLanguageDependentTypeFilter") \
  .facet("toolServiceInputOutputResourceTypeFilter") \
  .facet("toolServiceInputOutputMediaTypeFilter") \
  .facet("toolServiceAnnotationTypeFilter") \
  .facet("toolServiceAnnotationFormatFilter") \
  .facet("toolServiceEvaluatedFilter") \
  .facet("textTextGenreFilter") \
  .facet("textTextTypeFilter") \
  .facet("textRegisterFilter") \
  .facet("audioConversationalTypeFilter") \
  .facet("audioScenarioTypeFilter") \
  .facet("languageVarietyFilter")

urlpatterns = patterns('metashare.repository.views',
  url(r'^browse/(?P<resource_name>[\w\-]*)/(?P<object_id>\w+)/$',
    'view', name='browse'),
  url(r'^browse/(?P<object_id>\w+)/$',
    'view', name='browse'),
  url(r'^download/(?P<object_id>\w+)/$',
    'download', name='download'),
  url(r'^download_contact/(?P<object_id>\w+)/$',
    'download_contact', name='download_contact'),
  url(r'^search/$',
    search_view_factory(view_class=MetashareFacetedSearchView,
                        form_class=FacetedBrowseForm,
                        template='repository/search.html',
                        searchqueryset=sqs)),
)
