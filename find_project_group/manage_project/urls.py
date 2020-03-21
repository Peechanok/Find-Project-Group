
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('',views.home, name='find_ptoject_home'),
     path('login/',views.my_login, name='find_ptoject_login'),
     path('logout/',views.my_logout, name='find_ptoject_logout'),
     path('signin/',views.sign_in, name='find_ptoject_signin'),
     path('profile/changepassword/',views.change_password, name='find_ptoject_change_password'),
     path('profile/edit/update/<int:user_id>/',views.update_profile, name='find_ptoject_user_update'),
     path('profile/edit/',views.profile, name='find_ptoject_user_profile'),
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)