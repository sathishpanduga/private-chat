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

    def messages(self, otheruser):
        return chain(
            self.message_receiver.filter(sender=otheruser),
            self.message_sender.filter(receiver=otheruser),
        )


class Message(models.Model):
    sender = models.ForeignKey(ChatUser, related_name="message_sender")
    receiver = models.ForeignKey(ChatUser, related_name="message_receiver")
    message = models.TextField()

    def __str__(self):
        return "[{0}]: {1}".format(self.sender, self.message)


class Contact(models.Model):
    requester = models.ForeignKey(ChatUser, related_name="contact_requested")
    accepter = models.ForeignKey(ChatUser, related_name="contact_accepted")


class ContactRequest(models.Model):
    user = models.ForeignKey(ChatUser)
    requester = models.ForeignKey(ChatUser, related_name="contact_requester")
    message = models.TextField(null=True, blank=True)

