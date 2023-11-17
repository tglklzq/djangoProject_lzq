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

class EditCourseForm(forms.ModelForm):
    # 移除course_textbook_pic字段，因为它是不可编辑的
    class Meta:
        model = Course
        fields = ['course_name', 'course_hours', 'type_id', 'course_status', 'course_reqs', 'course_point', 'course_memo']

    # 添加一个额外的文件字段，用于处理上传的新图片
    new_course_textbook_pic = forms.ImageField(required=False, label='新书本封面')

    def save(self, commit=True):
        # 获取传递给表单的实例，即编辑前的课程对象
        instance = super().save(commit=False)

        # 获取新的图片，如果存在，则保存到课程对象中
        new_image = self.cleaned_data.get('new_course_textbook_pic')
        if new_image:
            instance.course_textbook_pic = new_image.read()

        # 如果commit参数为True，则保存到数据库
        if commit:
            instance.save()

        return instance
#////////////////////////////////////////////////////////////
class AddCourseTypeForm(forms.ModelForm):
    class Meta:
        model = CourseType
        fields = ['type_name']

class CourseTypeForm(forms.ModelForm):
    class Meta:
        model = CourseType
        fields = ['type_name', 'type_id']
        widgets = {
            'type_id': forms.HiddenInput(),
        }


class SearchCourseTypeForm(forms.Form):
    search_query = forms.CharField(label='搜索', max_length=255, required=True)

class CourseTypeForm(forms.Form):
    type_id = forms.IntegerField(required=True)
    type_name = forms.CharField(max_length=100, required=True)

class SearchForm(forms.Form):
    search_query = forms.CharField(label='搜索', max_length=100)