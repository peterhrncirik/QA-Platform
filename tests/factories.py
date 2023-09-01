import factory
from faker import Faker

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