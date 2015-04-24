from itertools import chain

from django.db import models
from django.contrib.auth.models import User, UserManager


class ChatUser(models.Model):
    user = models.OneToOneField(User)
    objects = UserManager()

    def get_username(self):
        return self.user.get_username()

    def contacts(self):
        return chain(
            map(lambda x: x.requester, self.contact_accepted.all()),
            map(lambda x: x.accepter, self.contact_requested.all())
        )

    def messages(self, otheruser):
        return sorted(list(chain(
            self.message_receiver.filter(sender=otheruser),
            self.message_sender.filter(receiver=otheruser),
        )), key=lambda x: x.created)


class Message(models.Model):
    sender = models.ForeignKey(ChatUser, related_name="message_sender")
    receiver = models.ForeignKey(ChatUser, related_name="message_receiver")
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} [{1}]: {2}".format(self.created.strftime('%H:%M:%S'), self.sender.get_username(), self.message)


class Contact(models.Model):
    requester = models.ForeignKey(ChatUser, related_name="contact_requested")
    accepter = models.ForeignKey(ChatUser, related_name="contact_accepted")


class ContactRequest(models.Model):
    user = models.ForeignKey(ChatUser)
    requester = models.ForeignKey(ChatUser, related_name="contact_requester")
    message = models.TextField(null=True, blank=True)

