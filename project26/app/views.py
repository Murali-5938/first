from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class tvwithdata(TemplateView):
    template_name='tvwithdata'
    def get_context_data(self, **kwargs):
        ecdo=super().get_context_data(**kwargs)
        ecdo['name']='krishna'
        return ecdo
    def post(self):
        
    
    