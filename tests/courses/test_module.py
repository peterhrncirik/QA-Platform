import pytest
from courses.models import Module

@pytest.fixture()
def new_module(db, new_module_factory, new_course):
    return new_module_factory(
        course=new_course, 
        title='Module 1', 
        description='New topics'
    )

def test_new_module(new_module):
    assert Module.objects.all().count() == 1
    assert new_module.title == 'Module 1'
    assert new_module.description == 'New topics'
    assert new_module.order == 0

def test_module_ordering(new_module, new_course):
    assert Module.objects.all().count() == 1
    module2 = Module.objects.create(course=new_course, title='Module 2', description='Module 2')
    assert Module.objects.all().count() == 2
    assert module2.order == 1
    module3 = Module.objects.create(course=new_course, title='Module 3', description='Module 3')
    assert Module.objects.all().count() == 3
    assert module3.order == 2

    # Custom order
    module4 = Module.objects.create(course=new_course, title='Module 3', description='Module 3', order=5)
    assert Module.objects.all().count() == 4
    assert module4.order == 5

def test_update_module(new_module):
    Module.objects.filter(title='Module 1').update(title='Module 2')
    module = Module.objects.get(title='Module 2')
    assert module.title == 'Module 2'

def test_delete_module(new_module):
    assert Module.objects.all().count() == 1
    Module.objects.get(title='Module 1').delete()
    assert Module.objects.all().count() == 0