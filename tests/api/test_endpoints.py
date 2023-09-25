import pytest
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