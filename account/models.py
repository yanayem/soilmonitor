from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):

    return f'user_{instance.user.id}/{filename}'
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True, default="Soil Analyst")
    last_email_change = models.DateTimeField(blank=True, null=True)

    @property
    def profile_pic_url(self):
        """Return URL of profile pic, safely."""
        if self.profile_pic and getattr(self.profile_pic, 'name', None):
            return self.profile_pic.url
        return None

    def __str__(self):
        return f"{self.user.username} Profile"
