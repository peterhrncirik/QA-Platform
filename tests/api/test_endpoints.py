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


