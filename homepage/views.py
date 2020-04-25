from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
class HomepageView(TemplateView):
        template_name = 'index.html'
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['my_statement'] = 'Nice to see you!'
                return context
        def say_bye(self): # add this line
                return 'Goodbye' # and this line too!