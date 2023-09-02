from django import forms
from django.forms.models import inlineformset_factory
from django.forms import ModelForm
from .models import Course, Module, Subject

class SubjectForm(ModelForm):

    class Meta:
        model = Subject
        fields = ['title', 'slug']

ModuleFormSet = inlineformset_factory(Course, 
                                      Module, 
                                      fields=[
                                          'title',
                                          'description',
                                      ],
                                      extra=2,
                                      can_delete=True)