import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_courses_view_logged_in(admin_client):

    """
        Tests Logged-In User
    """

    url = reverse('manage_course_list')
    response = admin_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_courses_view_redirect_not_logged_in(client):

    """
        Tests not Logged-In User
    """

    url = reverse('manage_course_list')
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.xfail(reason="URLs not implemented yet")
@pytest.mark.django_db
def test_module_create_content_view(admin_client):

    """
        Tests whether Logged-in User with Permissions Can Create a Module
    """

    url = reverse('module_content_create', kwargs={'module_id': 6, 'model_name': 'image'})
    response = admin_client.get(url)
    assert response.status_code == 200

@pytest.mark.xfail(reason="URLs not implemented yet")
@pytest.mark.django_db
def test_module_update_content_view(client):

    """
        Tests whether not Logged-in User is Redirected when Trying to Create new Course
    """

    url = reverse('module_content_create', kwargs={'module_id': 1, 'model_name': 'content'})
    response = client.get(url)
    assert response.status_code == 302