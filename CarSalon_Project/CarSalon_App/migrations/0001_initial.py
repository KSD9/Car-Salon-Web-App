# Generated by Django 2.2 on 2020-02-17 11:56

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarAstMar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('horsePowers', models.PositiveIntegerField()),
                ('engineType', models.CharField(max_length=200)),
                ('topSpeed', models.PositiveIntegerField()),
                ('zeroToHundredAcceleration', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('isForRent', models.BooleanField(default=False)),
                ('isRented', models.BooleanField(default=False)),
                ('sellingStatus', models.CharField(default='Available', max_length=300)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('RentManager', 'Rent Manager'), ('SalesManager', 'Sales Manager'), ('Administrator', 'Administrator')], max_length=300)),
                ('image', models.ImageField(upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SystemLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=300)),
                ('dateTime', models.DateTimeField()),
                ('model', models.CharField(max_length=300)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersSysLog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SoldCars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('carId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carsSold', to='CarSalon_App.CarAstMar')),
                ('employeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soldCarUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RentedCars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('carId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carsRented', to='CarSalon_App.CarAstMar')),
                ('employeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentCarUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateTimeField()),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('carId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carsApp', to='CarSalon_App.CarAstMar')),
            ],
        ),
    ]
