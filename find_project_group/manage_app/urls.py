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
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)