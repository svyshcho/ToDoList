from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from task.forms import TaskForm, TagForm
from task.models import Task, Tag
from django.urls import reverse_lazy


def index(request):
    tasks = Task.objects.all()

    context = {"tasks": tasks}

    return render(request, "task/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:main-page")
    template_name = "task/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:main-page")
    template_name = "task/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    context_object_name = "task"
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy("task:main-page")


def change_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()

    return redirect("task:main-page")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "task/tag_list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("task:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("task:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    context_object_name = "tag"
    template_name = "task/tag_confirm_delete.html"
    success_url = reverse_lazy("task:tags-list")
