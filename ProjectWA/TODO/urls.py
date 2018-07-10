from django.conf.urls import url
from TODO import views

urlpatterns = [
    url(r'^$',views.TaskListView.as_view(),name='task_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^task/new/$',views.CreateTaskView.as_view(),name='task_new'),
    url(r'^task/(?P<pk>\d+)/edit/$',views.UpdateTaskView.as_view(),name='task_edit'),
    url(r'^task/(?P<pk>\d+)/remove/$',views.TaskDeleteView.as_view(),name='task_remove'),
    url(r'^task/(?P<pk>\d+)/done/$',views.task_done,name='task_done'),


]