# Generated by Django 5.1.3 on 2024-11-08 04:27

import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(error_messages={'unique': 'error_email_exists'}, help_text="User's email address.", max_length=255, unique=True, verbose_name='Email Address')),
                ('email_verified_at', models.DateTimeField(help_text='The date and time when the email was verified.', null=True, verbose_name='Email Verification Date')),
                ('balance', models.IntegerField(default=0, help_text="User's current balance.", verbose_name='Balance')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('member', 'Member')], default='member', help_text='The role assigned to the user.', max_length=20, verbose_name='User Role')),
                ('password', models.CharField(help_text="User's password.", max_length=255, verbose_name='Password')),
                ('username', models.CharField(error_messages={'unique': 'error_username_exists'}, help_text='Username', max_length=255, unique=True, verbose_name='Username')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
