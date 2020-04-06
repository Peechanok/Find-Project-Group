
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('home/',views.home, name='find_project_home'),
     path('',views.my_login, name='find_project_login'),
     path('logout/',views.my_logout, name='find_project_logout'),
     path('signin/',views.sign_in, name='find_project_signin'),
     
     path('profile/edit/update/<int:user_id>/',views.update_profile, name='find_project_user_update'),
     path('profile/edit/',views.profile_user, name='find_project_user_profile'),
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)