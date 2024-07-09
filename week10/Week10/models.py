from django.db import models

# Create your models here.
# 데이터 저장 공간
class Student(models.Model):
    studentId = models.IntegerField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    admission = models.DateTimeField()


class Subject(models.Model):
    subjectId = models.IntegerField(primary_key=True)
    name = models.TextField()
    admission = models.DateTimeField()