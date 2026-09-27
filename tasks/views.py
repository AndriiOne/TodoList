from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from tasks.forms import TaskForm
from tasks.models import Tag, Task


class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TagListView(ListView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


class TaskToggleStatusView(View):

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("tasks:task-list")
