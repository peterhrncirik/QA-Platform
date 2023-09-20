import pytest

from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm

from django.contrib.auth.forms import UserCreationForm


@pytest.mark.parametrize('username, email, password1, password2,  validity', 
    [
        ('a'*151, 'test@test.com', 'p1', 'p1', False), # Username too long
        ('username', '', 'p1', 'p2', False), # Passwords do not match
        ('test', 'test@test.com', 'p1', 'p1', True), # Correct
        ('test', 'test@test', 'p1', 'p1', False), # Incorrect email 
    ],
)
def test_user_instance(db, user_factory, username, email, password1, password2, validity):

    form = CustomUserCreationForm(
        data={
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2,
        },
    )

    assert form.is_valid() is validity

