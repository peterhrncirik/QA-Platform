import pytest
from courses.models import Course


class TestCourses:

    def test_new_course(self, db, course_factory):

        course = course_factory()
        print(course.title)
        print(course.overview)
        assert Course.objects.all().count() == 1
        assert course.owner is not None

    def test_update_course(self, db, course_factory):

        course= course_factory()
        Course.objects.filter(title=course.title).update(title='Calculus')
        with pytest.raises(Exception):
            Course.objects.get(title='Algebra')

    def test_delete_course(self, db, course_factory):

        course = course_factory()
        assert Course.objects.all().count() == 1
        course.delete()
        assert Course.objects.all().count() == 0