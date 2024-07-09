from .models import Student
from .models import Subject
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__" # Json에 표시하는 모델 항목들을 모두 넣기

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"