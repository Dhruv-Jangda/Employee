from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    salary = models.BigIntegerField()

