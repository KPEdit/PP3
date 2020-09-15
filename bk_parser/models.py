from django import forms
import datetime
from django.db import models
from django.contrib.auth import models as umodels
from django.conf import settings
# from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

# Create your models here.


class BKUserManager(umodels.BaseUserManager):

    def create_user(self, password, username, name, last_name, email):
        user = self.model(
            username=username,
            name=name,
            last_name=last_name,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, username, name, last_name, email):
        user = self.create_user(
            password=password,
            username=username,
            name=name,
            last_name=last_name,
            email=email
        )
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class BKUser(umodels.AbstractBaseUser):

    class Meta:
        db_table = 'bk_user'
        verbose_name = "BKUser"
        verbose_name_plural = "BKUsers"

    objects = BKUserManager()

    username = models.CharField(
        max_length=60,
        unique=True
    )
    name = models.CharField(
        max_length=256
    )
    last_name = models.CharField(
        max_length=256
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )

    balance = models.FloatField(
        auto_created=True,
        default=0.0,
    )

    def __str__(self):
        return f"{self.last_name} {self.name}"

    def has_perm(self, app_label):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'last_name', 'email','password',]


class Sport(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class BetType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class SureBet(models.Model):
    url = models.CharField(max_length=2048)
    time = models.TimeField()
    date = models.DateField(default=datetime.date.today)
    t1 = models.CharField(max_length=64)
    t2 = models.CharField(max_length=64)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    k1 = models.FloatField()
    k2 = models.FloatField()
    bet_type = models.ForeignKey(BetType, on_delete=models.CASCADE)
    is_as = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sport.__str__().capitalize()} - {self.date} {self.time} | {self.t1}:{self.k1} - {self.t2}:{self.k2}"

    def __repr__(self):
        return f"{self.sport.__str__().capitalize()} - {self.date} {self.time} | {self.t1}:{self.k1} - {self.t2}:{self.k2}"

