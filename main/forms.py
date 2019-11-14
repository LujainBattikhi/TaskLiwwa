from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, ButtonHolder, Submit
from django import forms
import logging

logger = logging.getLogger('django')
from main.models import Candidates
from django.forms.widgets import DateInput

from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


class RegistrationForm(forms.ModelForm):
    """
          Form for Registration
    """

    class Meta:
        model = Candidates
        fields = ['full_name', 'dob', 'years_of_experience',
                  'department', 'resume']
        widgets = {
            'dob': DateInput(),
        }
