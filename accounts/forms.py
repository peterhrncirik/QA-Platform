from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

from .models import CustomUser

ROLES = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
)

class SimpleSignupForm(SignupForm):
    role = forms.ChoiceField(choices=ROLES, label='I am a:')
    field_order = ['username', 'email', 'password', 'role']

    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        if self.cleaned_data['role'] == 'student':
            student_group = Group.objects.get(name='Students')
            user.groups.add(student_group)
        elif self.cleaned_data['role'] == 'teacher':
            teacher_group = Group.objects.get(name='Instructors')
            user.groups.add(teacher_group)
        user.save()
        return user  
    
        

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)