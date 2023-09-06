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

