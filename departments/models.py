from django.db import models


class Department(models.Model):
    role_choices = [
        ("Republic", "Republic"),
        ("Region", "Region"),
        ("District", "District"),
        ("Neighborhood", "Neighborhood"),
    ]
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=role_choices, default="Republic")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
