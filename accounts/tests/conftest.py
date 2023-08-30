import pytest
from accounts.models import CustomUser


@pytest.fixture()
def new_user_factory(db):

    def create_app_user(
            username: str, 
            password: str = None,
            first_name: str = 'firstname',
            last_name: str = 'lastname',
            email: str = 'test@test.com',
            is_staff: bool = False,
            is_superuser: bool = False,
            is_active: bool = True,
        ):
        
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )

        return user

    return create_app_user

@pytest.fixture()
def user_Regular(db, new_user_factory):
    return new_user_factory('test_user', 'password', 'John')

@pytest.fixture()
def user_Admin(db, new_user_factory):
    return new_user_factory('admin_user', 'password', is_superuser=True)