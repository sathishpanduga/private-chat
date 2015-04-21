from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "private_chat/index.html"