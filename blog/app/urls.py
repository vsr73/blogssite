from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginuser,name='login'),
    path('blogregister/',views.createblog,name='createblog'),
    path('register',views.registeruser,name='registeruser'),
    path('logout/',views.logoutuser,name='logout'),
    path('delte/<str:pk>',views.deleteblog,name='deleteblog'),
    path('editblog/<str:pk>',views.editblog,name='editblog'),
    path('aboutus/',views.about,name="about"),
    path('contact/',views.bloggersupport,name='support'),
    path('profile/<str:pk>',views.userprofile,name='profile'),
    path('editprofile/<str:pk>',views.editprofile,name='editprofile'),
    path('blogprofileview/<str:pk>',views.blogprofileview,name='blogprofileview')
]