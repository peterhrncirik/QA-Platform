import factory
from faker import Faker

from django.contrib.auth.models import Group, Permission

from accounts.models import CustomUser
from courses.models import Course, Subject, Module

# Initialize Faker
fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CustomUser

    # Generate Dummy Data
    username = fake.name()
    is_staff = 'True'
    is_superuser = 'True'

class SubjectFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Subject

    title = 'Mathematics'
    slug = 'mathematics'

class CourseFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Course

    owner = factory.SubFactory(UserFactory)
    subject = factory.SubFactory(SubjectFactory)
    title = 'Algebra'
    slug = 'algebra'
    overview = 'Algebra 1'

class ModuleFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Module

    course = factory.SubFactory(CourseFactory)
    title = 'Algebra Basics'
    description = 'Introduction to Algebra'

class GroupFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Group

    name = 'Instructors'
    permissions = ['courses.add_course', 'courses.change_course', 'courses.view_course', 'courses.delete_course']