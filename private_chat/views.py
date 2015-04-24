from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin
from django.contrib.auth.models import User


class Index(TemplateView):
    template_name = "private_chat/index.html"


class ChatTemplate:
    def get_context_data(self, **kwargs):
        context = super(ChatTemplate, self).get_context_data(**kwargs)
        context['chatuser'] = self.request.user.chatuser
        return context


class Profile(LoginRequiredMixin, ChatTemplate, TemplateView):
    template_name = "private_chat/profile.html"


class Chat(LoginRequiredMixin, ChatTemplate, TemplateView):
    template_name = "private_chat/chat.html"

    def get_context_data(self, **kwargs):
        context = super(Chat, self).get_context_data(**kwargs)
        otheruser = User.objects.get(username=self.kwargs['username']).chatuser
        context['other_chatuser'] = otheruser
        context['chat_messages'] = self.request.user.chatuser.messages(otheruser)
        return context

