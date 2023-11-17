from django import forms

from myapp.model import Course, CourseType


class UpdateProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    number = forms.CharField(max_length=10)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'  # 或者你可以指定需要的字段

class DeleteCourseForm(forms.Form):
    course_no = forms.CharField(max_length=50, label='课程编号')

class AddCourseTypeForm(forms.ModelForm):
    class Meta:
        model = CourseType
        fields = ['type_name']

class SearchCourseTypeForm(forms.Form):
    search_query = forms.CharField(label='搜索', max_length=255, required=True)

class CourseTypeForm(forms.Form):
    type_id = forms.IntegerField(required=True)
    type_name = forms.CharField(max_length=100, required=True)

class SearchForm(forms.Form):
    search_query = forms.CharField(label='搜索', max_length=100)