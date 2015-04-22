from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender")
    receiver = models.ForeignKey(User, related_name="receiver")
    message = models.TextField()


class Contacts(models.Model):
    user1 = models.ForeignKey(User, related_name="user1")
    user2 = models.ForeignKey(User, related_name="user2")


class ContactRequests(models.Model):
    user = models.ForeignKey(User)
    requester = models.ForeignKey(User, related_name="requester")
    message = models.TextField(null=True, blank=True)

