from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

from .models import CustomUser
from courses.models import School

ROLES = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
)

class SimpleSignupForm(SignupForm):
    role = forms.ChoiceField(choices=ROLES, label='I am a:')
    school = forms.ModelChoiceField(queryset=School.objects.all(), empty_label='Select a school')
    field_order = ['username', 'email', 'password', 'role']

    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        school = School.objects.get(name=self.cleaned_data['school'])
        if self.cleaned_data['role'] == 'student':
            user.is_student = True
            school.students.add(user)
        elif self.cleaned_data['role'] == 'teacher':
            user.is_instructor = True
            school.instructors.add(user)
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