from django.urls import path
from . import views
from .views import ThemeView, TaskView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('add_task/<theme_id>', views.add_task, name='add_task'),
    path('update_task/<task_id>', views.update_task, name='update_task'),
    path('delete_task/<task_id>', views.delete_task, name='delete_task'),
    path('add_theme', views.add_theme, name='add_theme'),
    path('update_theme/<theme_id>', views.update_theme, name='update_theme'),
    path('delete_theme/<theme_id>', views.delete_theme, name='delete_theme'),
    path('api/themes/', ThemeView.as_view(), name='theme-list-create'),
    path('api/tasks/', TaskView.as_view(), name='task-list-create'),
    #path('api/get-token/', obtain_auth_token, name='get-token'),
]

