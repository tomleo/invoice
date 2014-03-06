from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^month/view/$', views.WorkMonthView.as_view(), name='work-month'),
    url(r'^month/create/$', views.WorkMonthCreate.as_view(), name='work-month-create'),
    url(r'^day/view/$', views.WorkDayView.as_view(), name='work-day'),
    url(r'^task/view/(?P<slug>\w+)/(?P<pk>\d+)/$', views.TaskView.as_view(), name='task-detail'),
)

