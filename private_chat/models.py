from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="message_sender")
    receiver = models.ForeignKey(User, related_name="message_receiver")
    message = models.TextField()


class Contact(models.Model):
    requester = models.ForeignKey(User, related_name="contact_requested")
    accepter = models.ForeignKey(User, related_name="contact_accepted")


class ContactRequest(models.Model):
    user = models.ForeignKey(User)
    requester = models.ForeignKey(User, related_name="contact_requester")
    message = models.TextField(null=True, blank=True)

