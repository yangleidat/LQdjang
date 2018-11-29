from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    #使用onetoonefield的含义是通过user这个字段声明UserProfile类与User类之间的关系一对一的
    user = models.OneToOneField(User, unique=True)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)