from django.forms import ModelForm

from cvservices.models import ActionTypeRequest, MethodTypeRequest, OrganizationTypeRequest, \
    SamplingFeatureGeotypeRequest, SamplingFeatureTypeRequest, SiteTypeRequest


class ActionTypeRequestForm(ModelForm):
    class Meta:

        model = ActionTypeRequest
        fields = ['term', 'name', 'definition', 'category', 'provenance', 'provenance_uri', 'produces_result',
                  'note', 'request_notes', 'submitter_name', 'submitter_email', 'request_reason']


class MethodTypeRequestForm(ModelForm):
    class Meta:

        model = MethodTypeRequest
        fields = ['term', 'name', 'definition', 'category', 'provenance', 'provenance_uri', 'note',
                  'request_notes', 'submitter_name', 'submitter_email', 'request_reason']


class OrganizationTypeRequestForm(ModelForm):
    class Meta:

        model = OrganizationTypeRequest
        fields = ['term', 'name', 'definition', 'category', 'provenance', 'provenance_uri', 'note',
                  'request_notes', 'submitter_name', 'submitter_email', 'request_reason']


class SamplingFeatureGeotypeRequestForm(ModelForm):
    class Meta:

        model = SamplingFeatureGeotypeRequest
        fields = ['term', 'name', 'definition', 'category', 'provenance', 'provenance_uri', 'note',
                  'request_notes', 'submitter_name', 'submitter_email', 'request_reason']


class SamplingFeatureTypeRequestForm(ModelForm):
    class Meta:

        model = SamplingFeatureTypeRequest
        fields = ['term', 'name', 'definition', 'category', 'provenance', 'provenance_uri', 'note',
                  'request_notes', 'submitter_name', 'submitter_email', 'request_reason']


class SiteTypeRequestForm(ModelForm):
    class Meta:

        model = SiteTypeRequest
        fields = ['term', 'name', 'definition', 'category', 'provenance', 'provenance_uri', 'note',
                  'request_notes', 'submitter_name', 'submitter_email', 'request_reason']
