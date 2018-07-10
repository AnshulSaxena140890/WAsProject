# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from TODO.models import Task
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from TODO.forms import TaskForm
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class TaskListView(ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(createdAt__lte=timezone.now()).order_by('createdAt')

class CreateTaskView(CreateView):
    form_class = TaskForm
    model = Task

class UpdateTaskView(UpdateView):
    form_class = TaskForm
    model = Task

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')


def task_done(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.Done()

    return redirect('task_list')