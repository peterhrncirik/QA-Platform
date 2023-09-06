import pytest
from accounts.models import CustomUser


def test_new_user(new_user):
    print('Groups: ', new_user.groups)
    assert CustomUser.objects.all().count() == 1


