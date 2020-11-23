from django.db import models

# Create your models here.


class ToDoList(models.Model):
    text = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
