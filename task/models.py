from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.content
