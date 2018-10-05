from django.urls import include, path
from . import views

app_name = 'blog'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('details/<int:id>/',views.details, name='details'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:id>/edit', views.post_edit, name='post_edit')
    #path('/form', views.form, name='form'),
    
    
    
]