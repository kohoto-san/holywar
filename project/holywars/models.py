from django.db import models
from django.contrib.auth.models import User

import datetime

from django import forms


class Holywar(models.Model):

    holywar_object_1 = models.CharField(max_length=20, default='True')
    holywar_description_1 = models.CharField(max_length=100, default='True')

    holywar_object_2 = models.CharField(max_length=20, default='True')
    holywar_description_2 = models.CharField(max_length=100, default='True')

    user = models.ForeignKey(User, blank=True, null=True)

    holywar_likes = models.IntegerField(default=0)
    threads = models.IntegerField(default=0)

    time_create = models.DateTimeField(auto_now_add=True, default='2000-10-10 10:10')

    def time_ago_create(self):

        create_time = self.time_create.replace(microsecond=0)
        now_time = datetime.datetime.now().replace(microsecond=0)
        now_time = now_time.replace(tzinfo=None)

        ago_time = now_time - create_time
        hours, remainder = divmod(ago_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        if ago_time.days >= 1:
            day = create_time.day
            month = create_time.strftime("%B")
            return "%s %s" % (day, month)
        elif hours > 0:
            hours = str(hours) + 'h ago'
            return hours
        else:
            minutes = str(minutes) + 'm ago'
            return minutes

    def __str__(self):
       return self.holywar_object_1 + ' VS. ' + self.holywar_object_2 + '  (' + str(self.id) + ')'


class HolywarLike(models.Model):

    holywar = models.ForeignKey('Holywar')
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.holywar.name


# НАДО ПЕРЕДЕЛАТЬ!
# модель с аргументами нахер не сдалась. Вместо это модели в качестве аргументов
# будут отображаться threads

class HolywarArgument(models.Model):

    holywar = models.ForeignKey('Holywar')
    argument_for = models.CharField(max_length=1, default='0')

    argument = models.CharField(max_length=100)

    def __str__(self):
        return self.argument + '  (' + str(self.holywar.id) + ')'


class Thread(models.Model):

    holywar = models.ForeignKey('Holywar')
    thread_likes = models.IntegerField(default=0)

    comments = models.IntegerField(default=0)

    description = models.CharField(max_length=200, default='True')
    name = models.CharField(max_length=100)

    user = models.ForeignKey(User, blank=True, null=True)

    argument_for = models.CharField(max_length=1, default='0')

    time_create = models.DateTimeField(auto_now_add=True)

    def time_ago_create(self):

        create_time = self.time_create.replace(microsecond=0)
        now_time = datetime.datetime.now().replace(microsecond=0)
        now_time = now_time.replace(tzinfo=None)

        ago_time = now_time - create_time
        hours, remainder = divmod(ago_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        if ago_time.days >= 1:
            day = create_time.day
            month = create_time.strftime("%B")
            return "%s %s" % (day, month)
        elif hours > 0:
            hours = str(hours) + 'h ago'
            return hours
        else:
            minutes = str(minutes) + 'm ago'
            return minutes

    def __str__(self):
        return self.name


class ThreadLike(models.Model):

    thread = models.ForeignKey('Thread')
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.thread.name


class ThreadComments(models.Model):

    thread = models.ForeignKey('Thread')
    comment_likes = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    avatar = models.CharField(max_length=50, default=0)

    text = models.TextField()

    user = models.ForeignKey(User, blank=True, null=True)

    def likes(self):
        return ThreadCommentsLike.objects.filter(comment=self).count()

    def time_ago_create(self):

        create_time = self.time_create.replace(microsecond=0)
        now_time = datetime.datetime.now().replace(microsecond=0)
        now_time = now_time.replace(tzinfo=None)

        ago_time = now_time - create_time
        hours, remainder = divmod(ago_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        if ago_time.days >= 1:
            day = create_time.day
            month = create_time.strftime("%B")
            return "%s %s" % (day, month)
        elif hours > 0:
            hours = str(hours) + 'h ago'
            return hours
        else:
            minutes = str(minutes) + 'm ago'
            return minutes

    def __str__(self):
        return self.name

    def __str__(self):
        return self.text


class ThreadCommentsLike(models.Model):

    comment = models.ForeignKey('ThreadComments')
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return str(self.comment.id)


class Invite(models.Model):

    code = models.CharField(max_length=30)

    def __str__(self):
        return self.code


class InviteForm(forms.Form):
    invite = forms.CharField(max_length=30)
