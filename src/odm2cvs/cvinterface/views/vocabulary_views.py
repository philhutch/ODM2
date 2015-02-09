from django.views.generic import ListView, DetailView

from cvservices.models import ActionType, MethodType, OrganizationType, SamplingFeatureGeotype, \
    SamplingFeatureType, SiteType


# list views
class VocabularyListView(ListView):
    pass


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
