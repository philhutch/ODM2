from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

from cvinterface.views import HomeView, ActionTypeDetailView, MethodTypeDetailView, OrganizationTypeDetailView, \
    SamplingFeatureGeotypeDetailView, SamplingFeatureTypeDetailView, SiteTypeDetailView

from cvinterface.views import action_type_view, method_type_view, organization_type_view, \
    sampling_feature_geotype_view, sampling_feature_type_view, site_type_view

from cvservices.api import ActionTypeResource, ActionTypeRequestResource, MethodTypeResource, \
    MethodTypeRequestResource, OrganizationTypeResource, OrganizationTypeRequestResource, \
    SamplingFeatureGeotypeResource, SamplingFeatureGeotypeRequestResource, SamplingFeatureTypeResource, \
    SamplingFeatureTypeRequestResource, SiteTypeResource, SiteTypeRequestResource

v1_api = Api(api_name='v1')
v1_api.register(ActionTypeResource())
v1_api.register(ActionTypeRequestResource())
v1_api.register(MethodTypeResource())
v1_api.register(MethodTypeRequestResource())
v1_api.register(OrganizationTypeResource())
v1_api.register(OrganizationTypeRequestResource())
v1_api.register(SamplingFeatureGeotypeResource())
v1_api.register(SamplingFeatureGeotypeRequestResource())
v1_api.register(SamplingFeatureTypeResource())
v1_api.register(SamplingFeatureTypeRequestResource())
v1_api.register(SiteTypeResource())
v1_api.register(SiteTypeRequestResource())

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^actiontype/$', action_type_view, name='actiontype'),
    url(r'^actiontype/(?P<pk>\w+)/$', ActionTypeDetailView.as_view(), name='actiontype_detail'),

    url(r'^methodtype/$', method_type_view, name='methodtype'),
    url(r'^methodtype/(?P<pk>\w+)/$', MethodTypeDetailView.as_view(), name='methodtype_detail'),

    url(r'^organizationtype/$', organization_type_view, name='organizationtype'),
    url(r'^organizationtype/(?P<pk>\w+)/$', OrganizationTypeDetailView.as_view(), name='organizationtype_detail'),

    url(r'^samplingfeaturegeotype/$', sampling_feature_geotype_view, name='samplingfeaturegeotype'),
    url(r'^samplingfeaturegeotype/(?P<pk>\w+)/$', SamplingFeatureGeotypeDetailView.as_view(), name='samplingfeaturegeotype_detail'),

    url(r'^samplingfeaturetype/$', sampling_feature_type_view, name='samplingfeaturetype'),
    url(r'^samplingfeaturetype/(?P<pk>\w+)/$', SamplingFeatureTypeDetailView.as_view(), name='samplingfeaturetype_detail'),

    url(r'^sitetype/$', site_type_view, name='sitetype'),
    url(r'^sitetype/(?P<pk>\w+)/$', SiteTypeDetailView.as_view(), name='sitetype_detail'),
)
