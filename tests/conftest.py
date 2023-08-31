import pytest
from accounts.models import CustomUser
from courses.models import Subject, Course, Module


@pytest.fixture()
def new_user_factory(db):

    def create_app_user(
            username: str, 
            password: str = None,
            first_name: str = 'firstname',
            last_name: str = 'lastname',
            email: str = 'test@test.com',
            is_staff: bool = False,
            is_superuser: bool = False,
            is_active: bool = True,
        ):
        
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )

        return user

    return create_app_user

@pytest.fixture()
def new_course_factory(db):

    def create_app_course(
            owner: int, 
            subject: str = None,
            title: str = None,
            slug: str = None,
            overview: str = None,
        ):
        
        course = Course.objects.create(
            owner=owner,
            subject=Subject.objects.create(title='Math', slug='math'),
            title=title,
            slug=slug,
            overview=overview
        )

        return course

    return create_app_course

@pytest.fixture()
def new_module_factory(db):

    def create_app_module(
            course: int, 
            title: str = None,
            description: str = None,
        ):
        
        module = Module.objects.create(
            course=course,
            title=title,
            description=description,
        )

        return module

    return create_app_module

@pytest.fixture()
def user_Regular(db, new_user_factory):
    return new_user_factory('test_user', 'password', 'John')

@pytest.fixture()
def user_Admin(db, new_user_factory):
    return new_user_factory('admin_user', 'password', is_superuser=True)

@pytest.fixture()
def new_course(db, new_course_factory, user_Regular):
    return new_course_factory(owner=user_Regular, subject='Mathematics', title='Algebra', slug='algebra', overview='Algebra basics')