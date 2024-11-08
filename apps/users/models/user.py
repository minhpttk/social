from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import TimestampsModel


class User(AbstractUser, TimestampsModel):
    class UserRole(models.TextChoices):
        ADMIN = "admin", "Admin"
        MEMBER = "member", "Member"
        
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="Email Address",
        help_text="User's email address.",
        error_messages={"unique": "error_email_exists"},
    )
    email_verified_at = models.DateTimeField(
        null=True,
        verbose_name="Email Verification Date",
        help_text="The date and time when the email was verified.",
    )
    balance = models.IntegerField(
        default=0, verbose_name="Balance", help_text="User's current balance."
    )
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.MEMBER,
        verbose_name="User Role",
        help_text="The role assigned to the user.",
    )
    password = models.CharField(
        max_length=255,
        verbose_name="Password",
        help_text="User's password.",
    )
    username = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Username",
        help_text="Username",
        error_messages={"unique": "error_username_exists"},
        
    )


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = "users"


    @property
    def is_email_verified(self):
        return bool(self.email_verified_at)

    def __str__(self) :
        return self.email
