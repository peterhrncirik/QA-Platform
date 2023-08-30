import pytest
from courses.models import Subject

@pytest.fixture()
def new_subject(db):
    return Subject.objects.create(title='Geography')

def test_create_new_subject(new_subject):
    assert Subject.objects.all().count() == 1

def test_delete_subject(new_subject):
    Subject.objects.get(title='Geography').delete()
    assert Subject.objects.all().count() == 0

def test_update_subject(new_subject):
    Subject.objects.filter(title='Geography').update(title='Mathematics')
    subject = Subject.objects.get(title='Mathematics')
    assert subject.title == 'Mathematics'


