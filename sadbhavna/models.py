from django.db import models


# Create your models here.

class Benner(models.Model):
    image = models.ImageField(upload_to="benner", editable=True, null=True, blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)
    contact = models.CharField(max_length=13, null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)


class WhatWeDo(models.Model):
    image = models.ImageField(upload_to="whatwedo", editable=True, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)


class Volunteer(models.Model):
    image = models.ImageField(upload_to="volunteer", editable=True, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)


class Cause(models.Model):
    image = models.ImageField(upload_to="causes", editable=True, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    raised = models.IntegerField(default=0, null=True, blank=True)
    goal = models.IntegerField(default=0, null=True, blank=True)


class LatestNews(models.Model):
    image = models.ImageField(upload_to="latestNews", editable=True, null=True, blank=True)
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=300, null=True, blank=True)


class UpcomingEvents(models.Model):
    image = models.ImageField(upload_to="upcomingEvent", editable=True, null=True, blank=True)
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=10000, null=True, blank=True)


class Contact(models.Model):
    fname = models.CharField(max_length=100, null=True, blank=True)
    lname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=300, default="", null=True, blank=True)
    subject = models.CharField(max_length=1000, null=True, blank=True)
    desc = models.CharField(max_length=100000, null=True, blank=True)
