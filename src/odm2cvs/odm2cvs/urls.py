from django.conf.urls import patterns, include, url
from django.contrib import admin

from cvservices.api import v1_api

from cvinterface.views.base_views import HomeView

from cvinterface.views.vocabulary_views import action_type_view, method_type_view, organization_type_view, \
    sampling_feature_geotype_view, sampling_feature_type_view, site_type_view

from cvinterface.views.vocabulary_views import ActionTypeDetailView, MethodTypeDetailView, OrganizationTypeDetailView, \
    SamplingFeatureGeotypeDetailView, SamplingFeatureTypeDetailView, SiteTypeDetailView

from cvinterface.views.request_views import SuccessRedirectView, action_type_request_create_view, method_type_request_create_view, \
    organization_type_request_create_view, sampling_feature_geotype_request_create_view, \
    sampling_feature_type_request_create_view, site_type_request_create_view


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^requests/success/(?P<vocabulary>\w+)/$', SuccessRedirectView.as_view(), name='request_success'),
    # url(r'^requests/actiontype, etc/$', ),

    url(r'^actiontype/$', action_type_view, name='actiontype'),
    url(r'^actiontype/(?P<pk>\w+)/$', ActionTypeDetailView.as_view(), name='actiontype_detail'),
    url(r'^actiontype/request$', action_type_request_create_view, name='actiontype_create'),

    url(r'^methodtype/$', method_type_view, name='methodtype'),
    url(r'^methodtype/(?P<pk>\w+)/$', MethodTypeDetailView.as_view(), name='methodtype_detail'),
    url(r'^methodtype/request$', method_type_request_create_view, name='methodtype_create'),

    url(r'^organizationtype/$', organization_type_view, name='organizationtype'),
    url(r'^organizationtype/(?P<pk>\w+)/$', OrganizationTypeDetailView.as_view(), name='organizationtype_detail'),
    url(r'^organizationtype/request$', organization_type_request_create_view, name='organizationtype_create'),

    url(r'^samplingfeaturegeotype/$', sampling_feature_geotype_view, name='samplingfeaturegeotype'),
    url(r'^samplingfeaturegeotype/(?P<pk>\w+)/$', SamplingFeatureGeotypeDetailView.as_view(), name='samplingfeaturegeotype_detail'),
    url(r'^samplingfeaturegeotype/request$', sampling_feature_geotype_request_create_view, name='samplingfeaturegeotype_create'),

    url(r'^samplingfeaturetype/$', sampling_feature_type_view, name='samplingfeaturetype'),
    url(r'^samplingfeaturetype/(?P<pk>\w+)/$', SamplingFeatureTypeDetailView.as_view(), name='samplingfeaturetype_detail'),
    url(r'^samplingfeaturetype/request$', sampling_feature_type_request_create_view, name='samplingfeaturetype_create'),

    url(r'^sitetype/$', site_type_view, name='sitetype'),
    url(r'^sitetype/(?P<pk>\w+)/$', SiteTypeDetailView.as_view(), name='sitetype_detail'),
    url(r'^sitetype/request$', site_type_request_create_view, name='sitetype_create'),
)
