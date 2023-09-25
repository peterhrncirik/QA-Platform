import factory

from django.contrib.auth.models import Group, Permission

from accounts.models import CustomUser
from courses.models import Course, Subject, Module

from tests.custom_providers import CustomProvider

# Add Subjects Provider
factory.Faker.add_provider(CustomProvider.school_subjects_provider())
factory.Faker.add_provider(CustomProvider.school_courses_provider())

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CustomUser

    username = factory.Faker('name')
    is_staff = 'True'
    is_superuser = 'True'

    @factory.post_generation
    def has_default_group(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            default_group, _ = Group.objects.get_or_create(
                name='group'
            )
            self.groups.add(default_group)

class SubjectFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Subject

    title = factory.Faker('school_subject')
    slug = factory.Sequence(lambda n: f'slug-{n}')

class CourseFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Course

    owner = factory.SubFactory(UserFactory)
    subject = factory.SubFactory(SubjectFactory)
    title = factory.Faker('school_course')
    slug = factory.Sequence(lambda n: f'slug-{n}')
    overview = factory.Faker('paragraph')

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