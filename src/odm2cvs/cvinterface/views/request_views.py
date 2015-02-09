from django.contrib import messages
from django.views.generic import CreateView, RedirectView
from django.core.urlresolvers import reverse, reverse_lazy

from cvinterface.forms import ActionTypeRequestForm, MethodTypeRequestForm, OrganizationTypeRequestForm, \
    SamplingFeatureGeotypeRequestForm, SamplingFeatureTypeRequestForm, SiteTypeRequestForm


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