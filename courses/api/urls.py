from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [

    # Subject - GET
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),

    # Course - POST
    path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),
]