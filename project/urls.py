from django.contrib import admin
from django.urls import path
from api.views import StudentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', StudentAPI.as_view(), name='student-api'),
]
