from django.db import models
from django.contrib.auth.models import *
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        
        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password, 
        )
        user.is_admin = True
        user.is_superuser=True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class UserModel(AbstractUser):
    email               = models.EmailField(max_length=25,               null=False, blank=False,    unique=True) 
    fullname            = models.CharField(max_length=2000) 
    createdAt           = models.DateTimeField(auto_now_add=True) 
    REQUIRED_FIELDS     = [] # <=must be mentioned in (model, create_superuser and create_user)
    USERNAME_FIELD      = "email"  # <=this no need add in (REQUIRED_FIELDS)
    objects = AccountManager()
