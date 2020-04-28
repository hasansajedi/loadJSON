# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_text as smart_unicode
from shortuuidfield import ShortUUIDField

import arrow


class BaseModel(models.Model):
    """
    Abstract model with for all models in our application.

    Attributes:
        created_at (DateTime): Description
        modified_at (DateTime): Description
        uuid (ShortUUID): Description
        archived (Boolean): Description
        deleted (Boolean): Description
    """
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Date Modified"), auto_now=True)
    uuid = ShortUUIDField(null=True, unique=True)
    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    creator = models.ForeignKey(User, related_name='email_creator', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        """Summary

        Attributes:
            abstract (bool): Description
        """
        abstract = True

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_at).humanize()


class EmailModel(BaseModel):
    id = models.AutoField(primary_key=True)
    id_got = models.BigIntegerField(null=False, blank=False)
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    imageUrl = models.URLField(max_length=250, null=False, blank=False)

    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")
        ordering = ('id',)

    def __unicode__(self) -> str:
        """
        Return a human readable representation of the model instance.
        Returns:
            string: The title of email
        """
        return smart_unicode("{}".format(self.title))

    def __str__(self) -> str:
        """
        Return a human readable representation of the model instance.
        Returns:
            string: The title of email
        """
        return smart_unicode("{}".format(self.title))
