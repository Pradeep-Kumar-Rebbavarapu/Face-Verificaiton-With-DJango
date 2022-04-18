from django.db import models
import random
import uuid
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
def user_directory_path(instance,filename):
    print(instance.id)
    return 'user_{0}/{1}'.format(instance.id,filename)

class User(AbstractUser):
    Username = None
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    email = models.EmailField(unique=True,null=True,blank=True)
    image = models.FileField(upload_to=user_directory_path)

    objects = UserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def name(self):
        return self.first_name + ' ' + self.last_name
