from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):

    STAR_CHOICES = (("1", u"One star"),
                    ("2", u"Two stars"),
                    ("3", u"Three stars"),
                    ("4", u"Four stars"),
                    ("5", u"Five stars"),
                    )

    name = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=250, default="", blank=True)
    rating = models.CharField(max_length=16, choices=STAR_CHOICES)
    website = models.CharField(max_length=128, default="", blank=True)



class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    # Or we could attach a client to the django User models:
    # user = models.OneToOneField(User, null=True, default=None, blank=True)


    phone = models.CharField(max_length=30, blank=True)
    work = models.CharField(max_length=64, default="", blank=True)


    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class Stay(models.Model):
    client = models.ForeignKey(Client)
    hotel = models.ForeignKey(Hotel)
    room = models.CharField(max_length=10, default="", blank=True)
    check_in = models.DateField()
    check_out = models.DateField()

    def __unicode__(self):
        return "%s @ %s from: %s to: %s" % (self.client.full_name(),
                                            self.hotel.name,
                                            self.check_in.strftime('%Y %m %d'),
                                            self.check_out.strftime('%Y %m %d'))

