from tastypie.resources import ModelResource
from models import ActionType, ActionTypeRequest, MethodType, MethodTypeRequest, \
    OrganizationType, OrganizationTypeRequest, SamplingFeatureGeotype, SamplingFeatureGeotypeRequest, \
    SamplingFeatureType, SamplingFeatureTypeRequest, SiteType, SiteTypeRequest


class ActionTypeResource(ModelResource):
    class Meta:
        queryset = ActionType.objects.all()
        resource_name = 'actiontypecv'
        max_limit = 0


class ActionTypeRequestResource(ModelResource):
    class Meta:
        queryset = ActionTypeRequest.objects.all()
        resource_name = 'actiontypecvrequest'
        max_limit = 0


class MethodTypeResource(ModelResource):
    class Meta:
        queryset = MethodType.objects.all()
        resource_name = 'methodtypecv'
        max_limit = 0


class MethodTypeRequestResource(ModelResource):
    class Meta:
        queryset = MethodTypeRequest.objects.all()
        resource_name = 'methodtypecvrequest'
        max_limit = 0


class OrganizationTypeResource(ModelResource):
    class Meta:
        queryset = OrganizationType.objects.all()
        resource_name = 'organizationtypecv'
        max_limit = 0


class OrganizationTypeRequestResource(ModelResource):
    class Meta:
        queryset = OrganizationTypeRequest.objects.all()
        resource_name = 'organizationtypecvrequest'
        max_limit = 0


class SamplingFeatureGeotypeResource(ModelResource):
    class Meta:
        queryset = SamplingFeatureGeotype.objects.all()
        resource_name = 'samplingfeaturegeotypecv'
        max_limit = 0


class SamplingFeatureGeotypeRequestResource(ModelResource):
    class Meta:
        queryset = SamplingFeatureGeotypeRequest.objects.all()
        resource_name = 'samplingfeaturegeotypecvrequest'
        max_limit = 0


class SamplingFeatureTypeResource(ModelResource):
    class Meta:
        queryset = SamplingFeatureType.objects.all()
        resource_name = 'samplingfeaturetypecv'
        max_limit = 0


class SamplingFeatureTypeRequestResource(ModelResource):
    class Meta:
        queryset = SamplingFeatureTypeRequest.objects.all()
        resource_name = 'samplingfeaturetypecvrequest'
        max_limit = 0


class SiteTypeResource(ModelResource):
    class Meta:
        queryset = SiteType.objects.all()
        resource_name = 'sitetypecv'
        max_limit = 0


class SiteTypeRequestResource(ModelResource):
    class Meta:
        queryset = SiteTypeRequest.objects.all()
        resource_name = 'sitetypecvrequest'
        max_limit = 0