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
    timeStart = models.TimeField()
    timeEnd = models.TimeField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return (self.title)


