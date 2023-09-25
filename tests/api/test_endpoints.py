import json 
import random

class TestSubjectEndpoints:

    endpoint = '/api/subjects/'

    def test_subject_get(self, subject_factory, api_client):

        """
            Get Request Returns all Subjects
        """
        
        # Number of Random 1-10 Subject Instaces
        n = random.randint(1, 10)

        # Arrange
        subject_factory.create_batch(n)

        # Act
        response = api_client().get(self.endpoint)

        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == n
    
    def test_subject_detail_get(self, subject_factory, api_client):

        """
            Returns Single Subject 
        """

        # Arrange
        subject = subject_factory()

        # Act
        response = api_client().get(f'{self.endpoint}{subject.id}/')

        # Assert
        assert response.status_code == 200
        assert 'id' in json.loads(response.content)
        assert 'title' in json.loads(response.content)
        assert 'slug' in json.loads(response.content)

class TestCourseEndpoints:

    endpoint = '/api/courses/'

    def test_course_enrollment_post(self, course_factory, api_client, user_factory):

        """
            Authenticated User can Enroll for a Course
        """

        # Arrange
        course = course_factory()
        user = user_factory()
        #TODO: Authenticate User

        # Act
        response = api_client().post(f'{self.endpoint}{course.id}/enroll/')

        # Assert
        assert response.status_code == 200

    def test_course_enrollment_unauthorized_user_post(self, course_factory, api_client):

        """
            Unauthorized User Can Not Enroll for a Course
        """

        # Arrange
        course = course_factory()

        # Act
        response = api_client().post(f'{self.endpoint}{course.id}/enroll/')

        # Assert
        assert response.status_code == 401




