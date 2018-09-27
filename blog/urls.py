from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^form', views.form, name='form'),
    url(r'^details/(?P<id>\d+)/$',views.details,name="details"),
    #url(r'^post/new', views.post_new, name='post_new'),
]