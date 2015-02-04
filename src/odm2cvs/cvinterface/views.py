from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse

from sys import modules
from inspect import getmembers, isclass

import cvservices.models
from cvservices.models import ControlVocabulary, ControlVocabularyRequest, ActionType, \
    MethodType, OrganizationType, SamplingFeatureGeotype, SamplingFeatureType, SiteType


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
    queryset = ActionType.objects.using('control_vocabularies')
    template_name = 'cvinterface/list.html'
    detail_view = None

    def get_context_data(self, **kwargs):
        context = super(ActionTypeView, self).get_context_data(**kwargs)
        urls = [reverse(self.detail_view, kwargs={'pk': cv.term}) for cv in context['object_list']]
        context['vocabulary_objects'] = zip(context['object_list'], urls)
        return context


class MethodTypeView(VocabularyListView):
    model = MethodType
    queryset = MethodType.objects.using('control_vocabularies')
    template_name = 'cvinterface/list.html'
    detail_view = None

    def get_context_data(self, **kwargs):
        context = super(MethodTypeView, self).get_context_data(**kwargs)
        urls = [reverse(self.detail_view, kwargs={'pk': cv.term}) for cv in context['object_list']]
        context['vocabulary_objects'] = zip(context['object_list'], urls)
        return context


class OrganizationTypeView(VocabularyListView):
    model = OrganizationType
    queryset = OrganizationType.objects.using('control_vocabularies')
    template_name = 'cvinterface/list.html'
    detail_view = None

    def get_context_data(self, **kwargs):
        context = super(OrganizationTypeView, self).get_context_data(**kwargs)
        urls = [reverse(self.detail_view, kwargs={'pk': cv.term}) for cv in context['object_list']]
        context['vocabulary_objects'] = zip(context['object_list'], urls)
        return context


class SamplingFeatureGeotypeView(VocabularyListView):
    model = SamplingFeatureGeotype
    queryset = SamplingFeatureGeotype.objects.using('control_vocabularies')
    template_name = 'cvinterface/list.html'
    detail_view = None

    def get_context_data(self, **kwargs):
        context = super(SamplingFeatureGeotypeView, self).get_context_data(**kwargs)
        urls = [reverse(self.detail_view, kwargs={'pk': cv.term}) for cv in context['object_list']]
        context['vocabulary_objects'] = zip(context['object_list'], urls)
        return context


class SamplingFeatureTypeView(VocabularyListView):
    model = SamplingFeatureType
    queryset = SamplingFeatureType.objects.using('control_vocabularies')
    template_name = 'cvinterface/list.html'
    detail_view = None

    def get_context_data(self, **kwargs):
        context = super(SamplingFeatureTypeView, self).get_context_data(**kwargs)
        urls = [reverse(self.detail_view, kwargs={'pk': cv.term}) for cv in context['object_list']]
        context['vocabulary_objects'] = zip(context['object_list'], urls)
        return context


class SiteTypeView(VocabularyListView):
    model = SiteType
    queryset = SiteType.objects.using('control_vocabularies')
    template_name = 'cvinterface/list.html'
    detail_view = None

    def get_context_data(self, **kwargs):
        context = super(SiteTypeView, self).get_context_data(**kwargs)
        urls = [reverse(self.detail_view, kwargs={'pk': cv.term}) for cv in context['object_list']]
        context['vocabulary_objects'] = zip(context['object_list'], urls)
        return context


# Detail Views
class ActionTypeDetailView(DetailView):
    model = ActionType
    queryset = ActionType.objects.using('control_vocabularies')
    template_name = 'cvinterface/term.html'


class MethodTypeDetailView(DetailView):
    model = MethodType
    queryset = MethodType.objects.using('control_vocabularies')
    template_name = 'cvinterface/term.html'


class OrganizationTypeDetailView(DetailView):
    model = OrganizationType
    queryset = OrganizationType.objects.using('control_vocabularies')
    template_name = 'cvinterface/term.html'


class SamplingFeatureGeotypeDetailView(DetailView):
    model = SamplingFeatureGeotype
    queryset = SamplingFeatureGeotype.objects.using('control_vocabularies')
    template_name = 'cvinterface/term.html'


class SamplingFeatureTypeDetailView(DetailView):
    model = SamplingFeatureType
    queryset = SamplingFeatureType.objects.using('control_vocabularies')
    template_name = 'cvinterface/term.html'


class SiteTypeDetailView(DetailView):
    model = SiteType
    queryset = SiteType.objects.using('control_vocabularies')
    template_name = 'cvinterface/term.html'


action_type_detail_view = ActionTypeDetailView.as_view()
method_type_detail_view = MethodTypeDetailView.as_view()
organization_type_detail_view = OrganizationTypeDetailView.as_view()
sampling_feature_geotype_detail_view = SamplingFeatureGeotypeDetailView.as_view()
sampling_feature_type_detail_view = SamplingFeatureTypeDetailView.as_view()
site_type_detail_view = SiteTypeDetailView.as_view()

action_type_view = ActionTypeView.as_view(detail_view=action_type_detail_view)
method_type_view = MethodTypeView.as_view(detail_view=method_type_detail_view)
organization_type_view = OrganizationTypeView.as_view(detail_view=organization_type_detail_view)
sampling_feature_geotype_view = SamplingFeatureGeotypeView.as_view(detail_view=sampling_feature_geotype_detail_view)
sampling_feature_type_view = SamplingFeatureTypeView.as_view(detail_view=sampling_feature_type_detail_view)
site_type_view = SiteTypeView.as_view(detail_view=site_type_detail_view)

view_functions = {ActionTypeView: action_type_view, MethodTypeView: method_type_view,
                  OrganizationTypeView: organization_type_view,
                  SamplingFeatureGeotypeView: sampling_feature_geotype_view,
                  SamplingFeatureTypeView: sampling_feature_type_view, SiteTypeView: site_type_view}


