from rest_framework.routers import SimpleRouter
from courses.apps import CoursesConfig
from courses.views import CourseViewSet
from django.urls import path

from courses.views import (
    LessonCreateAPIView,
    LessonUpdateAPIView,
    LessonRetrieveAPIView,
    LessonListAPIView,
    LessonDestroyAPIView,
)

app_name = CoursesConfig.name

router = SimpleRouter()
router.register("courses", CourseViewSet)
urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path(
        "lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
    path(
        "lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
]

urlpatterns += router.urls
