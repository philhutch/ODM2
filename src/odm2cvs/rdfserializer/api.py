from django.http import HttpResponse

from tastypie.bundle import Bundle
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from tastypie.utils.mime import build_content_type

from .models import Scheme, Namespace, Node, FieldRelation

from rdflib import Graph, URIRef, Literal
from rdflib import Namespace as ns
from rdflib.namespace import SKOS, RDF


class ModelRdfResource(ModelResource):
    scheme = None

    def create_response(self, request, data, response_class=HttpResponse,
                        **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.
        Mostly a useful shortcut/hook.
        """
        desired_format = self.determine_format(request)
        serialized = (
            self.serialize(request, data, desired_format,
                           options={'scheme': self.scheme}))

        return (response_class(content=serialized,
                content_type=build_content_type(desired_format),
                **response_kwargs))


class RdfSerializer(Serializer):
    formats = ['json', 'skos']
    content_types = {
        'json': 'application/json',
        'skos': 'text/plain'
        # 'skos': 'application/rdf+xml'
    }

    def to_skos(self, data, options=None):
        """
        Given some data, converts that data to an rdf skos format in xml.
        """
        # element = {}
        # get scheme: resource being requested. actionTypeCV, methodTypeCV, etc.
        scheme = Scheme.objects.get(name=options['scheme'])

        baseURI = 'http://vocabulary.hydroserver.org/ODM2/ODM2Terms/'
        graph = Graph()
        odm2 = ns(baseURI)
        dc = ns('http://purl.org/dc/elements/1.1/')

        graph.bind('odm2', odm2)
        graph.bind('skos', SKOS)
        graph.bind('dc', dc)

        # If requesting an entire CV.
        if isinstance(data, dict):
            # Add a SKOS ConceptScheme class to the graph.
            (graph.add((URIRef(scheme.uri), RDF['type'],
                        SKOS['ConceptScheme'])))
            (graph.add((URIRef(scheme.uri), dc['title'],
                        Literal(scheme.title))))
            (graph.add((URIRef(scheme.uri), dc['creator'],
                        Literal(scheme.creator))))
            (graph.add((URIRef(scheme.uri), dc['description'],
                        Literal(scheme.description))))

            # For each concept in the requested CV, create a SKOS Concept class.
            for concept in data[u'objects']:
                (graph.add((URIRef(scheme.uri + '/' + concept.obj.term),
                            RDF['type'], SKOS['Concept'])))
                (graph.add((URIRef(scheme.uri + '/' + concept.obj.term),
                            SKOS['inScheme'], URIRef(scheme.uri))))

                # Add labels to each concept class.
                for x in concept.data:
                    # Skip resource_uri and term elements.
                    # TODO: remove these elements entirely?
                    if x == u'resource_uri' or x == 'term':
                        continue
                    # Skip empty elements.
                    elif concept.data[x].rstrip('\r\n') == '':
                        continue
                    else:
                        alias = str(FieldRelation.objects.get(
                                    field_name=x).node.namespace)
                        if alias == 'odm2':
                            (graph.add((URIRef(scheme.uri + '/' +
                                        concept.obj.term),
                                        odm2[FieldRelation.objects
                                        .get(field_name=x).node.name],
                                        Literal(
                                        concept.data[x].rstrip('\r\n')))))
                        else:
                            (graph.add((URIRef(scheme.uri + '/' +
                                        concept.obj.term),
                                        SKOS[FieldRelation.objects
                                        .get(field_name=x).node.name],
                                        Literal(concept.data[x]
                                        .rstrip('\r\n')))))

        # If requesting a single Concept
        # TODO: Return the Concept Scheme as well.
        elif isinstance(data, Bundle):
            # Add a SKOS ConceptScheme class to the graph.
            (graph.add((URIRef(scheme.uri), RDF['type'],
                        SKOS['ConceptScheme'])))
            (graph.add((URIRef(scheme.uri), dc['title'],
                        Literal(scheme.title))))
            (graph.add((URIRef(scheme.uri), dc['creator'],
                        Literal(scheme.creator))))
            (graph.add((URIRef(scheme.uri), dc['description'],
                        Literal(scheme.description))))

            # Add a SKOS Concept class to the graph.
            (graph.add((URIRef(scheme.uri + '/' + data.obj.term),
                        RDF['type'], SKOS['Concept'])))
            (graph.add((URIRef(scheme.uri + '/' + data.obj.term),
                        SKOS['inScheme'], URIRef(scheme.uri))))

            # Add labels within concept class.
            for field in data.data.keys():
                if field == 'term' or field == u'resource_uri':
                    continue
                elif data.data[field].rstrip('\r\n') == '':
                    continue
                else:
                    relation = FieldRelation.objects.get(field_name=field)
                    alias = relation.node.namespace.alias
                    if alias == u'odm2':
                        (graph.add((URIRef(scheme.uri + '/' + data.obj.term),
                                    odm2[FieldRelation.objects
                                    .get(field_name=field).node.name],
                                    Literal(str(data.data[field]
                                                .rstrip('\r\n'))))))
                    else:
                        (graph.add((URIRef(scheme.uri + '/' + data.obj.term),
                                    SKOS[FieldRelation.objects
                                    .get(field_name=field).node.name],
                                    Literal(data.data[field].rstrip('\r\n')))))
        else:
            pass
        # Returning the graph serialized into 'xml' format rather than
        # 'pretty-xml' so that the Concept Scheme remains on its own level,
        # rather than inside one of the concepts.
        return graph.serialize(format='xml')
