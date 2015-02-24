from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from cvservices.api import v1_api

from cvinterface.views.base_views import HomeView

from cvinterface.views.vocabulary_views import action_type_view, method_type_view, organization_type_view, \
    sampling_feature_geotype_view, sampling_feature_type_view, site_type_view

from cvinterface.views.vocabulary_views import ActionTypeDetailView, MethodTypeDetailView, OrganizationTypeDetailView, \
    SamplingFeatureGeotypeDetailView, SamplingFeatureTypeDetailView, SiteTypeDetailView

from cvinterface.views.request_views import action_type_request_view, method_type_request_view, \
    organization_type_request_view, sampling_feature_geotype_request_view, sampling_feature_type_request_view, \
    site_type_request_view

from cvinterface.views.request_views import RequestsView, SuccessRedirectView, action_type_request_create_view, \
    method_type_request_create_view, organization_type_request_create_view, \
    sampling_feature_geotype_request_create_view, sampling_feature_type_request_create_view, \
    site_type_request_create_view

from cvinterface.views.request_views import ActionTypeRequestDetailView

urlpatterns = patterns('',
    url(r'^' + settings.SITE_URL + '$', HomeView.as_view(), name='home'),
    url(r'^' + settings.SITE_URL + 'api/', include(v1_api.urls)),
    url(r'^' + settings.SITE_URL + 'admin/', include(admin.site.urls)),

    # requests
    url(r'^' + settings.SITE_URL + 'requests/$', RequestsView.as_view(), name='requests_list'),
    url(r'^' + settings.SITE_URL + 'requests/success/(?P<vocabulary>\w+)/$', SuccessRedirectView.as_view(), name='request_success'),

    url(r'^' + settings.SITE_URL + 'requests/actiontype/$', action_type_request_view, name='actiontype_requests'),
    url(r'^' + settings.SITE_URL + 'requests/actiontype/new$', action_type_request_create_view, name='actiontype_create'),
    url(r'^' + settings.SITE_URL + 'requests/actiontype/(?P<pk>[-\w]+)$', ActionTypeRequestDetailView.as_view(), name='actiontype_request_detail'),

    url(r'^' + settings.SITE_URL + 'requests/methodtype/$', method_type_request_view, name='methodtype_requests'),
    url(r'^' + settings.SITE_URL + 'requests/methodtype/new', method_type_request_create_view, name='methodtype_create'),

    url(r'^' + settings.SITE_URL + 'requests/organizationtype/$', organization_type_request_view, name='organizationtype_requests'),
    url(r'^' + settings.SITE_URL + 'requests/organizationtype/new', organization_type_request_create_view, name='organizationtype_create'),

    url(r'^' + settings.SITE_URL + 'requests/samplingfeaturegeotype/$', sampling_feature_geotype_request_view, name='samplingfeaturegeotype_requests'),
    url(r'^' + settings.SITE_URL + 'requests/samplingfeaturegeotype/new', sampling_feature_geotype_request_create_view, name='samplingfeaturegeotype_create'),

    url(r'^' + settings.SITE_URL + 'requests/samplingfeaturetype/$', sampling_feature_type_request_view, name='samplingfeaturetype_requests'),
    url(r'^' + settings.SITE_URL + 'requests/samplingfeaturetype/new', sampling_feature_type_request_create_view, name='samplingfeaturetype_create'),

    url(r'^' + settings.SITE_URL + 'requests/sitetype/$', site_type_request_view, name='sitetype_requests'),
    url(r'^' + settings.SITE_URL + 'requests/sitetype/new', site_type_request_create_view, name='sitetype_create'),

    # vocabularies
    url(r'^' + settings.SITE_URL + 'actiontype/$', action_type_view, name='actiontype'),
    url(r'^' + settings.SITE_URL + 'actiontype/(?P<pk>\w+)/$', ActionTypeDetailView.as_view(), name='actiontype_detail'),

    url(r'^' + settings.SITE_URL + 'methodtype/$', method_type_view, name='methodtype'),
    url(r'^' + settings.SITE_URL + 'methodtype/(?P<pk>\w+)/$', MethodTypeDetailView.as_view(), name='methodtype_detail'),

    url(r'^' + settings.SITE_URL + 'organizationtype/$', organization_type_view, name='organizationtype'),
    url(r'^' + settings.SITE_URL + 'organizationtype/(?P<pk>\w+)/$', OrganizationTypeDetailView.as_view(), name='organizationtype_detail'),

    url(r'^' + settings.SITE_URL + 'samplingfeaturegeotype/$', sampling_feature_geotype_view, name='samplingfeaturegeotype'),
    url(r'^' + settings.SITE_URL + 'samplingfeaturegeotype/(?P<pk>\w+)/$', SamplingFeatureGeotypeDetailView.as_view(), name='samplingfeaturegeotype_detail'),

    url(r'^' + settings.SITE_URL + 'samplingfeaturetype/$', sampling_feature_type_view, name='samplingfeaturetype'),
    url(r'^' + settings.SITE_URL + 'samplingfeaturetype/(?P<pk>\w+)/$', SamplingFeatureTypeDetailView.as_view(), name='samplingfeaturetype_detail'),

    url(r'^' + settings.SITE_URL + 'sitetype/$', site_type_view, name='sitetype'),
    url(r'^' + settings.SITE_URL + 'sitetype/(?P<pk>\w+)/$', SiteTypeDetailView.as_view(), name='sitetype_detail'),

)
