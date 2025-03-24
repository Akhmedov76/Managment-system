from django.db import models
from tasks.models import Task

class Report(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=500)
    
    def __str__(self):
        return f"Report for {self.task.title}"