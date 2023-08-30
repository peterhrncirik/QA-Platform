import pytest

def test_username(user_Regular):
    assert user_Regular.username == 'test_user'

def test_admin(user_Admin):
    assert user_Admin.is_superuser