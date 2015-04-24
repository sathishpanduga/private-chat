from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin

from private_chat.models import ChatUser


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
        otheruser = ChatUser.objects.get(username=self.kwargs['username'])
        context['other_chatuser'] = otheruser
        context['chat_messages'] = self.request.user.chatuser.messages(otheruser)
        return context

