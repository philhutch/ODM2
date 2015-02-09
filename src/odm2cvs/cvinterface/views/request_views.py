from sys import modules
from inspect import getmembers, isclass

from django.contrib import messages
from django.views.generic import ListView, CreateView, RedirectView
from django.core.urlresolvers import reverse, reverse_lazy

import cvservices.models
from cvservices.models import ControlVocabulary, ControlVocabularyRequest, ActionTypeRequest, MethodTypeRequest, \
    OrganizationTypeRequest, SamplingFeatureGeotypeRequest, SamplingFeatureTypeRequest, SiteTypeRequest

from cvinterface.forms import ActionTypeRequestForm, MethodTypeRequestForm, OrganizationTypeRequestForm, \
    SamplingFeatureGeotypeRequestForm, SamplingFeatureTypeRequestForm, SiteTypeRequestForm


# list views
class RequestListView(ListView):
    pass


class RequestsView(ListView):
    queryset = []
    template_name = 'cvinterface/requests/main_requests_list.html'

    def get_context_data(self, **kwargs):
        context = super(RequestsView, self).get_context_data(**kwargs)
        models = [(obj, obj.__name__, obj._meta.verbose_name)
                  for member, obj in getmembers(cvservices.models, isclass)
                  if issubclass(obj, ControlVocabularyRequest)
                  and issubclass(obj, ControlVocabulary)
                  and not obj._meta.abstract]

        views = [(obj.model.__name__, obj)
                 for view, obj in getmembers(modules[__name__], isclass)
                 if issubclass(obj, RequestListView)
                 and obj is not RequestListView]

        context['requests'] = [{'name': verbose_name, 'url': reverse(view_functions[view]), 'model_name': model_name}
                               for model, class_name, verbose_name in models
                               for model_name, view in views
                               if class_name == model_name]

        context['pending_requests'] = [(pending_object, pending_object._meta.verbose_name)
                                       for model, model_name, verbose_name in models
                                       for pending_object in model.objects.filter(status='Pending')
                                       if model.objects.filter(status='Pending').count() > 0]
        # TODO: ^ when detail views of this are made, update this to link to the detail of each pending concept

        return context


class ActionTypeRequestView(RequestListView):
    model = ActionTypeRequest
    template_name = 'cvinterface/requests/actiontype_request_list.html'


class MethodTypeRequestView(RequestListView):
    model = MethodTypeRequest
    template_name = 'cvinterface/requests/methodtype_request_list.html'


class OrganizationTypeRequestView(RequestListView):
    model = OrganizationTypeRequest
    template_name = 'cvinterface/requests/organizationtype_request_list.html'


class SamplingFeatureGeotypeRequestView(RequestListView):
    model = SamplingFeatureGeotypeRequest
    template_name = 'cvinterface/requests/samplingfeaturegeotype_request_list.html'


class SamplingFeatureTypeRequestView(RequestListView):
    model = SamplingFeatureTypeRequest
    template_name = 'cvinterface/requests/samplingfeaturetype_request_list.html'


class SiteTypeRequestView(RequestListView):
    model = SiteTypeRequest
    template_name = 'cvinterface/requests/sitetype_request_list.html'

action_type_request_view = ActionTypeRequestView.as_view()
method_type_request_view = MethodTypeRequestView.as_view()
organization_type_request_view = OrganizationTypeRequestView.as_view()
sampling_feature_geotype_request_view = SamplingFeatureGeotypeRequestView.as_view()
sampling_feature_type_request_view = SamplingFeatureTypeRequestView.as_view()
site_type_request_view = SiteTypeRequestView.as_view()


view_functions = {ActionTypeRequestView: action_type_request_view, MethodTypeRequestView: method_type_request_view,
                  OrganizationTypeRequestView: organization_type_request_view,
                  SamplingFeatureGeotypeRequestView: sampling_feature_geotype_request_view,
                  SamplingFeatureTypeRequestView: sampling_feature_type_request_view,
                  SiteTypeRequestView: site_type_request_view}


# create views
action_type_request_create_view = CreateView.as_view(
    template_name='cvinterface/requests/actiontype_form.html', form_class=ActionTypeRequestForm,
    success_url=reverse_lazy('request_success', kwargs={'vocabulary': 'actiontype'}))

method_type_request_create_view = CreateView.as_view(
    template_name='cvinterface/requests/methodtype_form.html', form_class=MethodTypeRequestForm,
    success_url=reverse_lazy('request_success', kwargs={'vocabulary': 'methodtype'}))

organization_type_request_create_view = CreateView.as_view(
    template_name='cvinterface/requests/organizationtype_form.html', form_class=OrganizationTypeRequestForm,
    success_url=reverse_lazy('request_success', kwargs={'vocabulary': 'organizationtype'}))

sampling_feature_geotype_request_create_view = CreateView.as_view(
    template_name='cvinterface/requests/samplingfeaturegeotype_form.html', form_class=SamplingFeatureGeotypeRequestForm,
    success_url=reverse_lazy('request_success', kwargs={'vocabulary': 'samplingfeaturegeotype'}))

sampling_feature_type_request_create_view = CreateView.as_view(
    template_name='cvinterface/requests/samplingfeaturetype_form.html', form_class=SamplingFeatureTypeRequestForm,
    success_url=reverse_lazy('request_success', kwargs={'vocabulary': 'samplingfeaturetype'}))

site_type_request_create_view = CreateView.as_view(
    template_name='cvinterface/requests/sitetype_form.html', form_class=SiteTypeRequestForm,
    success_url=reverse_lazy('request_success', kwargs={'vocabulary': 'sitetype'}))


class SuccessRedirectView(RedirectView):
    message = "Your request for a new concept has been made."

    def get_redirect_url(self, vocabulary):
        messages.add_message(self.request, messages.SUCCESS, self.message)
        # TODO: if user is an administrator, redirect to the list of requests.
        return reverse(vocabulary)