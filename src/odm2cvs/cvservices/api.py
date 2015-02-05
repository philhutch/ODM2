from tastypie.api import Api
from tastypie.resources import ModelResource

from rdfserializer.api import RdfSerializer, ModelRdfResource
from models import ActionType, ActionTypeRequest, MethodType, MethodTypeRequest, \
    OrganizationType, OrganizationTypeRequest, SamplingFeatureGeotype, SamplingFeatureGeotypeRequest, \
    SamplingFeatureType, SamplingFeatureTypeRequest, SiteType, SiteTypeRequest


class ActionTypeResource(ModelRdfResource):
    scheme = 'actionTypeCV'

    class Meta:
        queryset = ActionType.objects.using('control_vocabularies').all()
        resource_name = 'actiontypecv'
        max_limit = 0
        serializer = RdfSerializer()



class ActionTypeRequestResource(ModelResource):
    class Meta:
        queryset = ActionTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'actiontypecvrequest'
        max_limit = 0


class MethodTypeResource(ModelResource):
    scheme = 'methodTypeCV'

    class Meta:
        queryset = MethodType.objects.using('control_vocabularies').all()
        resource_name = 'methodtypecv'
        max_limit = 0


class MethodTypeRequestResource(ModelResource):
    class Meta:
        queryset = MethodTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'methodtypecvrequest'
        max_limit = 0


class OrganizationTypeResource(ModelResource):
    scheme = 'organizationTypeCV'

    class Meta:
        queryset = OrganizationType.objects.using('control_vocabularies').all()
        resource_name = 'organizationtypecv'
        max_limit = 0


class OrganizationTypeRequestResource(ModelResource):
    class Meta:
        queryset = OrganizationTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'organizationtypecvrequest'
        max_limit = 0


class SamplingFeatureGeotypeResource(ModelResource):
    scheme = 'samplingFeatureGeotypeCV'

    class Meta:
        queryset = SamplingFeatureGeotype.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturegeotypecv'
        max_limit = 0


class SamplingFeatureGeotypeRequestResource(ModelResource):
    class Meta:
        queryset = SamplingFeatureGeotypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturegeotypecvrequest'
        max_limit = 0


class SamplingFeatureTypeResource(ModelResource):
    scheme = 'samplingFeatureTypeCV'

    class Meta:
        queryset = SamplingFeatureType.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturetypecv'
        max_limit = 0


class SamplingFeatureTypeRequestResource(ModelResource):
    class Meta:
        queryset = SamplingFeatureTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'samplingfeaturetypecvrequest'
        max_limit = 0


class SiteTypeResource(ModelResource):
    scheme = 'siteTypeCV'

    class Meta:
        queryset = SiteType.objects.using('control_vocabularies').all()
        resource_name = 'sitetypecv'
        max_limit = 0


class SiteTypeRequestResource(ModelResource):
    class Meta:
        queryset = SiteTypeRequest.objects.using('control_vocabularies').all()
        resource_name = 'sitetypecvrequest'
        max_limit = 0


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