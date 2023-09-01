import pytest
from courses.models import Course

def test_new_course(new_course):
    assert Course.objects.all().count() == 1
    assert new_course.owner is not None
    assert new_course.title == 'Algebra'
    assert new_course.slug == 'algebra'
    assert new_course.overview == 'Algebra 1'

def test_update_course(new_course):
    Course.objects.filter(title='Algebra').update(title='Calculus')
    with pytest.raises(Exception):
        Course.objects.get(title='Algebra')

def test_delete_course(new_course):
    assert Course.objects.all().count() == 1
    new_course.delete()
    assert Course.objects.all().count() == 0