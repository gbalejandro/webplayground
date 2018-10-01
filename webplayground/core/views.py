from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Mi super Web Playground2'})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"