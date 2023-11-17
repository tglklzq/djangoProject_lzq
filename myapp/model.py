from django.db import models


class User(models.Model):
    user_number = models.CharField(max_length=10, primary_key=True)  # 指定user_number为主键
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'


class Course(models.Model):
    course_no = models.CharField(max_length=50, primary_key=True)
    course_name = models.CharField(max_length=100)
    course_hours = models.IntegerField()
    type_id = models.IntegerField()
    course_status = models.CharField(max_length=1)
    course_reqs = models.CharField(max_length=20)
    course_point = models.DecimalField(max_digits=3, decimal_places=0)
    course_memo = models.CharField(max_length=1000, null=True, blank=True)
    course_textbook_pic = models.BinaryField(null=True, blank=True)

    class Meta:
        db_table = 'course'

class CourseType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.type_name
    class Meta:
        db_table = 'course_type'
