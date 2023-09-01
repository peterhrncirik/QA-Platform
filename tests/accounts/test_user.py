import pytest
from accounts.models import CustomUser

@pytest.mark.django_db
def test_new_user(user_factory):
    user_factory.create()
    assert CustomUser.objects.all().count() == 1

# def test_admin(user_Admin):
#     assert user_Admin.is_superuser