from django.shortcuts import render

from django.views.generic import ListView, CreateView, DetailView

from .models import Day, Month, Task

class WorkMonthView(ListView):

    context_object_name = 'workmonth'
    model = Month
    template_name = 'work/work_month.html'

class WorkMonthCreate(CreateView):

    context_object_name = 'workmonth'
    model = Month
    template_name = 'work/work_month_create.html'

class WorkDayView(ListView):

    context_object_name = 'workday'
    model = Day
    template_name = 'work/work_day.html'

class TaskView(DetailView):

    context_object_name = 'task'
    model = Task
    template_name = 'work/task.html'
    queryset = Task.objects.all()

