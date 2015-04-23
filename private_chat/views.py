from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin


class Index(TemplateView):
    template_name = "private_chat/index.html"


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "private_chat/profile.html"
    login_url = reverse_lazy('private-chat:login')
