from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]
    success_url = reverse_lazy("show_my_tasks")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/mine.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    # template_name = "recipes/edit.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
