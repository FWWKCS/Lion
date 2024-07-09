from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        StudentSerializer = self.get_serializer(data=request.data)
        StudentSerializer.is_valid(raise_exception=True)
        self.perform_create(StudentSerializer)
        headers = self.get_success_headers(StudentSerializer.data)
        return Response(StudentSerializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        StudentSerializer = self.get_serializer(instance)
        return Response(StudentSerializer.data)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            StudentSerializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(StudentSerializer.data)
        
        StudentSerializer = self.get_serializer(queryset, many=True)
        return Response(StudentSerializer.data)
    