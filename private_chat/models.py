from itertools import chain

from django.db import models
from django.contrib.auth.models import User


class ChatUser(User):
    user = models.OneToOneField(User)

    def contacts(self):
        return chain(
            map(lambda x: x.requester, self.contact_accepted.all()),
            map(lambda x: x.accepter, self.contact_requested.all())
        )


class Message(models.Model):
    sender = models.ForeignKey(ChatUser, related_name="message_sender")
    receiver = models.ForeignKey(ChatUser, related_name="message_receiver")
    message = models.TextField()


class Contact(models.Model):
    requester = models.ForeignKey(ChatUser, related_name="contact_requested")
    accepter = models.ForeignKey(ChatUser, related_name="contact_accepted")


class ContactRequest(models.Model):
    user = models.ForeignKey(ChatUser)
    requester = models.ForeignKey(ChatUser, related_name="contact_requester")
    message = models.TextField(null=True, blank=True)

