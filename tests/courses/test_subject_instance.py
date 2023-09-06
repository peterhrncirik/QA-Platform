import pytest
from courses.models import Subject
from courses.forms import SubjectForm

@pytest.mark.parametrize('title, slug, validity', 
    [
        ('Algebra', 'algebra', True),
        ('', '', False),
        ('a'*201, 'slug', False), # Checks for too long title
        ('title', '', False),
    ],
)
def test_subject_instance(db, subject_factory, title, slug, validity):

    form = SubjectForm(
        data={
            'title': title,
            'slug': slug,
        },
    )    

    assert form.is_valid() is validity