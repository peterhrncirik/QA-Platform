import pytest
from pytest_factoryboy import register
from factories import UserFactory, CourseFactory, SubjectFactory, ModuleFactory

# Register Factories
register(UserFactory)
register(CourseFactory)
register(SubjectFactory)
register(ModuleFactory)


@pytest.fixture
def new_user(db, user_factory):
    user = user_factory.create()
    return user

@pytest.fixture
def new_course(db, course_factory):
    course = course_factory.create()
    return course

@pytest.fixture
def new_subject(db, subject_factory):
    subject = subject_factory.create()
    return subject

@pytest.fixture
def new_module(db, module_factory):
    module = module_factory.create()
    return module