
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords

# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,  password = None, **extra_fields):
        return self._create_user(username, email, name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, password = None, **extra_fields ):
        return self._create_user(username, email, name,  password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=45, unique=True ,blank=True, null=True)
    email = models.EmailField('Correo Electronico', max_length=45, unique=True,blank=True, null=True)
    name = models.CharField('Nombres',max_length=45,blank=True, null=True)
    Last_name = models.CharField('Apellidos', max_length=45, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def natural_key(self):
        return (self.username) 

    def __str__(self):
        return f'{self.name}'

