from django.urls import path
from course import views
urlpatterns=[
    path('course',views.CourseList.as_view()),
    path('course/<int:pk>',views.CourseDetails.as_view())
]