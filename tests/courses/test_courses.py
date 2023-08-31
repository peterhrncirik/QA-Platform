import pytest
from courses.models import Course

def test_new_course(new_course):
    assert Course.objects.all().count() == 1
    assert new_course.title == 'Algebra'
    assert new_course.slug == 'algebra'
    assert new_course.overview == 'Algebra basics'

def test_update_course(new_course):
    Course.objects.filter(title='Algebra').update(title='Calculus')
    course = Course.objects.get(title='Calculus')
    assert course.title == 'Calculus'

def test_delete_course(new_course):
    assert Course.objects.all().count() == 1
    Course.objects.get(title='Algebra').delete()
    assert Course.objects.all().count() == 0