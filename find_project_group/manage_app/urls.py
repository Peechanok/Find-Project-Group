from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
 path('course/',views.selectCouse, name='find_project_couse'),
 path('add_course/',views.viewaddCourse, name='add_course'),
 path('add_course/add/',views.addCourse, name='add_course_submits') ,  
 path('view_course/',views.viewCourse, name='view_course') ,
  path('view_course/delete/<int:course_id>/',views.deleteCourse, name='delete_course') ,
 path('project/',views.selectProject, name='find_project_project'),
 path('add_project/',views.viewaddProject, name='add_project'),
 path('add_project/add/',views.addProject, name='add_project_submits') ,
 path('view_project/',views.viewProject, name='view_project') ,
  path('view_project/delete/<int:course_id>/',views.deleteProject, name='delete_project') ,
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)