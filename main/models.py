from __future__ import unicode_literals

# Create your models here.

from enum import Enum
import logging

from django.core.validators import FileExtensionValidator
from django.db import models

logger = logging.getLogger('django')


class Department(Enum):
    IT = 'it'
    HR = 'hr'
    FINANCE = 'finance'


# Create your models here.
class Candidates(models.Model):
    full_name = models.CharField(max_length=336)
    dob = models.DateField()
    years_of_experience = models.PositiveIntegerField()
    department = models.CharField(max_length=255,
                                  choices=[(department.name, department.value) for department in Department],
                                  default=Department.IT.name)
    resume = models.FileField(upload_to='uploads/', blank=False, null=False,
                              validators=[FileExtensionValidator(['pdf', 'docx', ])])
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
