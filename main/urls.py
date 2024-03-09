from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create/<theme_id>', views.create, name='create'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('delete_event/<task_id>', views.delete_event, name='delete-event'),
    path('update/<task_id>', views.update, name='update'),
    path('add_theme', views.add_theme, name='add_theme'),
    path('delete_theme/<theme_id>', views.delete_theme, name='delete_theme'),
]
