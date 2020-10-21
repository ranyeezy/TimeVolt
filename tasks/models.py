from django.db import models






class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return (self.title)


