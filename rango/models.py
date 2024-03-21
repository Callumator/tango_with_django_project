from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    number_of_cats = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
class Cat(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
