import pytest
from accounts.models import CustomUser

def test_new_user(new_user):
    assert CustomUser.objects.all().count() == 1
