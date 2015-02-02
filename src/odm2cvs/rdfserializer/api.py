from django.http import HttpResponse

from tastypie.bundle import Bundle
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from tastypie.utils.mime import build_content_type

from .models import Scheme, Namespace, Node, FieldRelation


class ModelRdfResource(ModelResource):
    scheme = None

    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.
        Mostly a useful shortcut/hook.
        """
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format, options={'scheme': self.scheme})
        return response_class(content=serialized, content_type=build_content_type(desired_format), **response_kwargs)


class RdfSerializer(Serializer):
    formats = ['json', 'skos']
    content_types = {
        'json': 'application/json',
        'skos': 'text/plain'
        # TODO: use 'skos': 'application/rdf+xml' after testing.
    }

    def to_skos(self, data, options=None):
        """
        Given some data, converts that data to an rdf skos format in xml.
        """
        element = {}
        # get scheme: resource being requested. actionTypeCV, methodTypeCV, etc.
        scheme = Scheme.objects.get(name=options['scheme'])
        if isinstance(data, dict):
            if u'objects' in data:
                # TODO: create ConceptScheme with the data from scheme.
                # TODO: for each bundle in u'objects': create skos:hasTopConcept with
                pass
            else:
                # weird...
                pass
        elif isinstance(data, Bundle):
            # TODO: for each data.data.keys() as fieldName:
            # TODO: create Concept. get namespace and node type as FieldRelation.objects.get(field_name=fieldName).node
            pass
        else:
            # uhm...
            pass

        return element