from django.views.generic import TemplateView


class BirdInterface(TemplateView):
    template_name = 'react_birds_list.jinja'
