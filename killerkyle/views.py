from django.views.generic import TemplateView
from django import forms

class homePage(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs): 
        context = super(homePage, self).get_context_data(**kwargs)
        return context
    
    def get(self, request, *args, **kwargs):
        return super(homePage, self).get(request, *args, **kwargs)