from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from courses.models import Subject, Course
from courses.api.serializers import SubjectSerializer, CourseSerializer, CourseWithContentsSerializer
from courses.api.permissions import IsEnrolled

class SubjectListView(generics.ListAPIView):

    """
    Returns a list of all subjects.
    """

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):

    """
    Returns a detail view of specific subject.
    """
    
    #TODO: Rewrite to ViewSet
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
        
class CourseViewSet(viewsets.ReadOnlyModelViewSet):

    """
    Courses ViewSet
    enroll() -> enrolls user to a specific course
    contents() -> returns a list of all contents of specific course
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'], authentication_classes=[BasicAuthentication], permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})
        
    #TODO: Test
    @action(detail=True, methods=['get'], serializer_class=CourseWithContentsSerializer, authentication_classes=[BasicAuthentication], permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

