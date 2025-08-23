from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Shift(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Shift {self.date} {self.start_time}-{self.end_time}"
    
class ShiftAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignments", null=False)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name="assignments", null=False)

    class Meta: 
        unique_together = ("user", "shift")

    def __str__(self):
        return f"{self.user.username}-{self.shift}"