import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from courses.views import CourseListView

urlpatterns = [
    path(os.environ.get('ADMIN_URL'), admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('course/', include('courses.urls')),
    path('courses/', CourseListView.as_view(), name='courses_list'),
    path('students/', include('students.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ] + urlpatterns
