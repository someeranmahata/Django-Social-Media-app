from django.urls import path
from . import views
app_name='activity'
urlpatterns = [
    path('postcreate/', views.post_create, name='post_create'),
]