import pytest
from courses.models import Subject

class TestSubject:

    def test_new_subject(self, new_subject):
        assert Subject.objects.all().count() == 1
        assert new_subject.title == 'Mathematics'
        assert new_subject.slug == 'mathematics'

    def test_update_subject(self, new_subject):
        Subject.objects.filter(title='Mathematics').update(title='Geography')
        with pytest.raises(Exception):
            Subject.objects.get(title='Mathematics')

    def test_delete_subject(self, new_subject):
        assert Subject.objects.all().count() == 1
        new_subject.delete()
        assert Subject.objects.all().count() == 0