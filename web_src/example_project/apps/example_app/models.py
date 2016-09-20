from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.core import validators


class Example(models.Model):
    """
    An Example model with various fields being filled out.
    """

    # the name of the example
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            validators.MinLengthValidator(2)
        ]
    )

    def get_absolute_url(self):
        return reverse('examples:view_example', args=[str(self.id)])

    def __str__(self):
        return str(self.name)
