from django.shortcuts import render
from projects.models import Project
from django.views.generic.list import ListView


class ProjectListView(ListView):
    model = Project
    template_name = "projects/list.html"
