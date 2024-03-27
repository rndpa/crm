from django.shortcuts import render
from django.views.generic import CreateView, TemplateView


class IndexView(TemplateView):
    template_name = 'CRM_WEB/index.html'
