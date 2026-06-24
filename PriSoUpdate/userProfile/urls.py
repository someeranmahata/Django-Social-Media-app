from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[

    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
     path(
        'follow/<str:username>/',
        views.follow_user,
        name='follow'
    ),

    path(
        'unfollow/<str:username>/',
        views.unfollow_user,
        name='unfollow'
    ),
    path('<str:username>/', views.profile_view, name='profile'),
   
]