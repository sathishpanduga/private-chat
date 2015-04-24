from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin


class Index(TemplateView):
    template_name = "private_chat/index.html"


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "private_chat/profile.html"
    login_url = reverse_lazy('private-chat:login')

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['chatuser'] = self.request.user.chatuser
        return context
