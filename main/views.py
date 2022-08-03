from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter

from .models import *
from .serializers import TeacherSerializer, StudentsSerializer


# class TeacherListView(generics.ListAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


class Search(generics.ListAPIView):
    """Поиск"""
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

