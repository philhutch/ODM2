from inspect import getmembers, isclass

from django.views.generic import ListView
from django.core.urlresolvers import reverse

import vocabulary_views
import cvservices.models
from vocabulary_views import VocabularyListView, view_functions
from cvservices.models import ControlVocabulary, ControlVocabularyRequest


class HomeView(ListView):
    queryset = []
    template_name = 'cvinterface/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        models = [(obj.__name__, obj._meta.verbose_name)
                  for member, obj in getmembers(cvservices.models, isclass)
                  if issubclass(obj, ControlVocabulary)
                  and not issubclass(obj, ControlVocabularyRequest)
                  and not obj._meta.abstract]

        views = [(obj.model.__name__, obj)
                 for view, obj in getmembers(vocabulary_views, isclass)
                 if issubclass(obj, VocabularyListView)
                 and obj is not VocabularyListView]

        context['vocabularies'] = [{'name': verbose_name, 'url': reverse(view_functions[view]), 'model_name': model_name}
                                   for class_name, verbose_name in models
                                   for model_name, view in views
                                   if class_name == model_name]

        return context