from django.db import models
from django.contrib.auth.models import User

# TODO implement profiles
# TODO bios
# TODO tie bot with new profiles
# TODO Guild ID's User ID's onto profiles of each User

class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='images/')
    bio = models.TextField(blank=True)
    twitch = models.CharField(blank=True, max_length=100)
    # disc_gid = models.CharField(max_length=200)
    disc_uid = models.CharField(max_length=200)
    exp = models.IntegerField(default=0)
    lvl = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def add_exp(self):
        new_exp = self.exp + 2
        return int(new_exp)

    def __str__(self):
        return f'{self.disc_uid} Profile'
