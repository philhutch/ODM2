from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse

from sys import modules
from inspect import getmembers, isclass

import cvservices.models
from cvservices.models import ControlVocabulary, ControlVocabularyRequest, ActionType, \
    MethodType, OrganizationType, SamplingFeatureGeotype, SamplingFeatureType, SiteType

from cvservices.models import ActionTypeRequest

from cvinterface.forms import ActionTypeRequestForm


class VocabularyListView(ListView):
    pass


class HomeView(ListView):
    queryset = []
    template_name = 'cvinterface/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        models = [(obj.__name__, obj._meta.verbose_name)
                  for member, obj in getmembers(cvservices.models, isclass)
                  if issubclass(obj, ControlVocabulary)
                  and not issubclass(obj, ControlVocabularyRequest)
                  and not obj._meta.abstract]

        views = [(obj.model.__name__, obj)
                 for view, obj in getmembers(modules[__name__], isclass)
                 if issubclass(obj, VocabularyListView)
                 and obj is not VocabularyListView]

        context['vocabularies'] = [{'name': verbose_name, 'url': reverse(view_functions[view]), 'model_name': model_name}
                                   for class_name, verbose_name in models
                                   for model_name, view in views
                                   if class_name == model_name]

        return context


class ActionTypeView(VocabularyListView):
    model = ActionType
    template_name = 'cvinterface/vocabularies/actiontype_list.html'


class MethodTypeView(VocabularyListView):
    model = MethodType
    template_name = 'cvinterface/vocabularies/methodtype_list.html'


class OrganizationTypeView(VocabularyListView):
    model = OrganizationType
    template_name = 'cvinterface/vocabularies/organizationtype_list.html'


class SamplingFeatureGeotypeView(VocabularyListView):
    model = SamplingFeatureGeotype
    template_name = 'cvinterface/vocabularies/samplingfeaturegeotype_list.html'


class SamplingFeatureTypeView(VocabularyListView):
    model = SamplingFeatureType
    template_name = 'cvinterface/vocabularies/samplingfeaturetype_list.html'


class SiteTypeView(VocabularyListView):
    model = SiteType
    template_name = 'cvinterface/vocabularies/sitetype_list.html'


# Detail Views
class ActionTypeDetailView(DetailView):
    model = ActionType
    template_name = 'cvinterface/vocabularies/actiontype_detail.html'


class MethodTypeDetailView(DetailView):
    model = MethodType
    template_name = 'cvinterface/vocabularies/methodtype_detail.html'


class OrganizationTypeDetailView(DetailView):
    model = OrganizationType
    template_name = 'cvinterface/vocabularies/organizationtype_detail.html'


class SamplingFeatureGeotypeDetailView(DetailView):
    model = SamplingFeatureGeotype
    template_name = 'cvinterface/vocabularies/samplingfeaturegeotype_detail.html'


class SamplingFeatureTypeDetailView(DetailView):
    model = SamplingFeatureType
    template_name = 'cvinterface/vocabularies/samplingfeaturetype_detail.html'


class SiteTypeDetailView(DetailView):
    model = SiteType
    template_name = 'cvinterface/vocabularies/sitetype_detail.html'


# list views
action_type_view = ActionTypeView.as_view()
method_type_view = MethodTypeView.as_view()
organization_type_view = OrganizationTypeView.as_view()
sampling_feature_geotype_view = SamplingFeatureGeotypeView.as_view()
sampling_feature_type_view = SamplingFeatureTypeView.as_view()
site_type_view = SiteTypeView.as_view()


view_functions = {ActionTypeView: action_type_view, MethodTypeView: method_type_view,
                  OrganizationTypeView: organization_type_view,
                  SamplingFeatureGeotypeView: sampling_feature_geotype_view,
                  SamplingFeatureTypeView: sampling_feature_type_view, SiteTypeView: site_type_view}

# create views
action_type_request_create_view = CreateView.as_view(template_name='cvinterface/requests/actiontype_form.html',
                                                     form_class=ActionTypeRequestForm)