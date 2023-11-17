# myapp/urls.py
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import login_view, success_view, register_view, page_view, page5_view, update_profile_view, page1_view, \
    edit_course_view, delete_course_view, page2_view, edit_course_type_view, delete_course_type_view, \
    add_course_type_view, search_course_type_view, search_courses_type

urlpatterns = [
    path('login/', login_view, name='login'),
    path('success/', success_view, name='success'),
    path('register/', register_view, name='register'),
    path('page/<int:page_number>/', page_view, name='page'),
    path('page5/<str:user_number>/', page5_view, name='page5'),
    path('update_profile/', update_profile_view, name='update_profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('update_profile/', update_profile_view, name='update_profile'),

    path('page1/', page1_view, name='page1'),
    path('edit_course/<str:course_no>/', edit_course_view, name='edit_course'),
    path('delete_course/<str:course_no>/', delete_course_view, name='delete_course'),

path('search_courses_type/', search_courses_type, name='search_courses_type'),



    path('page2/', page2_view, name='page2'),
    path('add_course_type/', add_course_type_view, name='add_course_type'),
    path('edit_course_type/<int:type_id>/', edit_course_type_view, name='edit_course_type'),
    path('delete_course_type/<int:type_id>/', delete_course_type_view, name='delete_course_type'),
    path('search_course_type/', search_course_type_view, name='search_course_type'),

]
