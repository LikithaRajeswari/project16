from django.db import models

# Create your models here.


class School(models.Model):
    SchName=models.CharField(max_length=100,primary_key=True)
    SchPricipal=models.CharField(max_length=100)
    SchLocation=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.SchName

class Student(models.Model):
    SchName=models.ForeignKey(School,on_delete=models.CASCADE)
    StuName=models.CharField(max_length=100)
    StuId=models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.StuName