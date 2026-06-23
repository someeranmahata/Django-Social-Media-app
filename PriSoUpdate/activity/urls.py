from django.urls import path
from . import views
app_name='activity'
urlpatterns = [
    path('postcreate/', views.post_create, name='post_create'),
    path('post/<int:post_id>/comment/',views.post_comment,name='post_comment'),
]