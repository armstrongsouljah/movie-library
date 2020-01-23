from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email cannot be blank')
        if not password:
            raise ValueError('Password cannot be left blank')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.staff = True
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.admin = True
        user.staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    registered = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def get_username(self):
        return self.email.split('@')[0]

    def is_active(self):
        return self.is_active

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    def get_short_name(self):
        return self.email.split('@')[0]

    def get_full_name(self):
        return self.email
