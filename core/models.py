from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_field):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email),**extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # 管理者画面にアクセスできるかどうか
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    # どのフィールドを認証に使うか(emailをIDとして使用)
    USERNAME_FIELD = "email"
