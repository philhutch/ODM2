from django.http import HttpResponse

from tastypie.bundle import Bundle
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from tastypie.utils.mime import build_content_type

from .models import Scheme, Namespace, Node, FieldRelation

from rdflib import Graph, URIRef, RDF, Literal
from rdflib import Namespace as ns


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


        baseURI = 'http://vocabulary.hydroserver.org/ODM2/'
        graph = Graph()
        skos = ns('http://www.w3.org/2004/02/skos/core#')
        odm2 = ns(baseURI)
        dc = ns('http://purl.org/dc/elements/1.1/')

        graph.bind('odm2', odm2)
        graph.bind('skos', skos)
        graph.bind('dc', dc)


        if isinstance(data, dict):
            if u'objects' in data:
                print type(scheme.title), scheme.title
                graph.add((URIRef(scheme.uri), RDF['type'], skos['ConceptScheme']))
                graph.add((URIRef(scheme.uri), dc['title'], Literal(scheme.title)))
                graph.add((URIRef(scheme.uri), dc['creator'], Literal(scheme.creator)))
                graph.add((URIRef(scheme.uri), dc['description'], Literal(scheme.description)))

                for concept in data[u'objects']:
                    graph.add((URIRef(scheme.uri + '/' + concept.obj.term), RDF['type'], skos['Concept']))
                    graph.add((URIRef(scheme.uri + '/' + concept.obj.term), skos['inScheme'], URIRef(scheme.uri)))
                    #graph.add((URIRef(scheme.uri + '/' + concept.data[u'term']), RDF['type'], skos['Concept']))
                    for x in concept.data:
                        if x != u'resource_uri' and x != 'term':
                            alias = str(FieldRelation.objects.get(field_name=x).node.namespace)
                            if alias == 'odm2':
                                graph.add((URIRef(scheme.uri + '/' + concept.obj.term), odm2[FieldRelation.objects.get(field_name=x).node.name], Literal(concept.data[x])))
                            else:
                                graph.add((URIRef(scheme.uri + '/' + concept.obj.term), skos[FieldRelation.objects.get(field_name=x).node.name], Literal(concept.data[x])))
            else:
                # weird...
                pass
        elif isinstance(data, Bundle):
            graph.add((URIRef(scheme.uri + '/' + data.obj.term), RDF['type'], skos['Concept']))
            graph.add((URIRef(scheme.uri + '/' + data.obj.term), skos['inScheme'], URIRef(scheme.uri)))
            for field in data.data.keys():
                if field == 'term' or field == u'resource_uri':
                    continue
                else:
                    relation = FieldRelation.objects.get(field_name=field)
                    alias = relation.node.namespace.alias
                    if alias == u'odm2':
                        graph.add((URIRef(scheme.uri + '/' + data.obj.term), odm2[FieldRelation.objects.get(field_name=field).node.name], Literal(data.data[field])))
                    else:
                        graph.add((URIRef(scheme.uri + '/' + data.obj.term), skos[FieldRelation.objects.get(field_name=field).node.name], Literal(data.data[field])))
            
        else:
            # uhm...
            pass
        return graph.serialize(format='pretty-xml')
        #return data[u'objects']
