import pytest
from courses.models import Subject

class TestSubject:

    def test_new_subject(self, db, subject_factory):
        
        # Create New Subject
        subject_factory()
        assert Subject.objects.all().count() == 1

    def test_update_subject(self, db, subject_factory):

        # Create New Subject
        subject = subject_factory()

        Subject.objects.filter(title=subject.title).update(title='Geography')

        with pytest.raises(Exception):
            Subject.objects.get(title='Mathematics')

    def test_delete_subject(self, db, subject_factory):

        subject = subject_factory()
        assert Subject.objects.all().count() == 1
        subject.delete()
        assert Subject.objects.all().count() == 0