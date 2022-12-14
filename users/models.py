from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    location = models.CharField(max_length=300, blank=True)
    #gender = models.CharField(verbose_name=_("Gender"), max_length=7)
    date_of_birth = models.DateField(verbose_name=_("Date of birth"), blank=True, null=True)
    address = models.CharField(verbose_name=_("Home Address"), max_length=1000, blank=True, null=True)
    city = models.CharField(verbose_name=_("City"), max_length=100, blank=True, null=True)
    zip_code = models.CharField(verbose_name=_("Postal Code"), max_length=15, blank=True, null=True)
    # phone_number = RegexValidator(regex=r"^\+(?:[0-9]@?){6,14}[0-9]$", message=_("Enter a valid phone number"))
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    photo = models.ImageField(verbose_name=_("Photo"), upload_to="photo/", default="photo/default-user-avatar.png")

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name
