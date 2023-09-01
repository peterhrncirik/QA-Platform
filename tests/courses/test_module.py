import pytest
from courses.models import Module

def test_new_module(new_module):
    assert Module.objects.all().count() == 1
    assert new_module.course is not None
    assert new_module.title == 'Algebra Basics'
    assert new_module.description == 'Introduction to Algebra'

def test_update_Module(new_module):
    Module.objects.filter(title='Algebra Basics').update(title='Calculus')
    with pytest.raises(Exception):
        Module.objects.get(title='Algebra Basics')

def test_delete_Module(new_module):
    assert Module.objects.all().count() == 1
    new_module.delete()
    assert Module.objects.all().count() == 0

# def test_module_ordering(new_module, new_Module):
#     assert Module.objects.all().count() == 1
#     module2 = Module.objects.create(Module=new_Module, title='Module 2', description='Module 2')
#     assert Module.objects.all().count() == 2
#     assert module2.order == 1
#     module3 = Module.objects.create(Module=new_Module, title='Module 3', description='Module 3')
#     assert Module.objects.all().count() == 3
#     assert module3.order == 2

#     # Custom order
#     module4 = Module.objects.create(Module=new_Module, title='Module 3', description='Module 3', order=5)
#     assert Module.objects.all().count() == 4
#     assert module4.order == 5
