from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    NURSE = "nurse"
    HEAD_NURSE = "head_nurse"
    ROLE_CHOICES = [(NURSE, "Nurse"), (HEAD_NURSE, "Head Nurse")]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=NURSE)

    nurse_id = models.CharField(max_length=10, unique=True, editable=False, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.nurse_id:
            prefix = "HN" if self.role == self.HEAD_NURSE else "NR"

            last_profile = (
                UserProfile.objects.filter(role=self.role, nurse_id__startswith=prefix).order_by("nurse_id").last()
            )

            if last_profile:
                last_num = int(last_profile.nurse_id.replace(prefix, ""))
                new_num = last_num +1
            else:
                new_num = 1

            self.nurse_id = f"{prefix}{new_num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}  ({self.role})"
