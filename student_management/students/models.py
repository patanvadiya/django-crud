from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.TextField()
    hobby = models.CharField(max_length=255,default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class StudentImage(models.Model):
    student_id = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/')
    # def __str__(self):
    #     return f"Image for Student ID: {self.student_id}"