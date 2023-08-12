from django.urls import path

from task.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    change_status,
    TagsListView,
    TagsUpdateView,
    TagsCreateView,
    TagsDeleteView,
)

urlpatterns = [
    path("", index, name="main-page"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/change/", change_status, name="task-change-status"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags-delete"),
]

app_name = "task"
