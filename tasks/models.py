from django.db import models



# Create your models here.
DAYS = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'),
)



class Task(models.Model):
    title = models.CharField(max_length=200)
    day = models.CharField(max_length= 1, choices=DAYS, default="0")
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return (self.title)


