"""
Definition of models.
"""

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 128)
    branch = models.CharField(max_length = 128)
    semester = models.CharField(max_length = 1)

    def __str__(self):
        return self.name


class Subject(models.Model):
    students = models.ForeignKey(Student, on_delete = models.CASCADE)
    sub_name = models.CharField(max_length = 128)


class Lecture(models.Model):
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    date = models.CharField(max_length = 20)


class Attendance(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete = models.CASCADE)
    student = models.ForeignKey(Subject, on_delete = models.CASCADE)
    attendance = models.CharField(max_length = 1)

