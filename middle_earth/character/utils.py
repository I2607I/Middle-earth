from .models import *
from django.db.models import Count

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('characters'))
        #cats = Category.objects.all()
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context