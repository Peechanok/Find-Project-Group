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
  path('addproject_ex/<int:student_id>/',views.addpro_ex, name='find_project_add_pro_ex') ,
   path('add_project_ex/',views.viewpro_ex, name='find_project_view_pro_ex') ,
 path('project/<int:course_id>/',views.selectProject, name='find_project_project'),
 path('add_project/add/<int:course_id>/',views.addProject, name='add_project_submits') ,
  path('view_project/delete/<int:course_id>/<int:project_id>/',views.deleteProject, name='delete_project') ,

path('view_group/<int:course_id>/<int:project_id>/',views.viewGroup, name='view_group') ,
path('view_group/<int:course_id>/<int:project_id>/add',views.addGroup, name='add_group') ,
path('view_group/<int:course_id>/<int:project_id>/<int:group_id>/delete',views.deleteGroup, name='delete_group') ,
path('view_group/<int:course_id>/<int:project_id>/<int:group_id>/',views.viewMember, name='view_member') ,
path('view_group/load/<int:group_id>/',views.loadMember, name='loadMember') ,
path('view_group/delete/<int:group_id>/<int:user_id>/',views.deleteMember, name='deleteMember') ,
 

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)