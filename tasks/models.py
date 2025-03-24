from django.db import models
from users.models import CustomUser
from departments.models import Department


class Task(models.Model):
    status_choices = [
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
        ("Returned", "Returned"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default="New",
        db_index=True,
        help_text="Current status of the task",
    )
    deadline = models.DateTimeField()
    created_by = models.ForeignKey(
        CustomUser, related_name="created_tasks", on_delete=models.CASCADE
    )
    assigned_to = models.ForeignKey(
        CustomUser,
        related_name="assigned_tasks",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    parent_task = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title


class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    from_department = models.ForeignKey(
        Department, related_name="sent_tasks", on_delete=models.CASCADE
    )
    to_department = models.ForeignKey(
        Department, related_name="received_tasks", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    status_change = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.task.title} - {self.status_change}"
