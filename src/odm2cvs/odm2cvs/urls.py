from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

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
    # Examples:
    # url(r'^$', 'odm2cvs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
