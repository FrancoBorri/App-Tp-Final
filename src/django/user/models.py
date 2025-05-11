from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class User_profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )  # One-to-one relationship with User model (inverse relationship)
    address = models.TextField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    picture_profile = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "user_profile"
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ["user"]
