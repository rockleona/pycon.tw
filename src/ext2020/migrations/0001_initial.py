# Generated by Django 3.0.7 on 2020-08-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True, verbose_name='token')),
                ('verified', models.BooleanField(default=False, verbose_name='verified')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('verified_at', models.DateTimeField(blank=True, null=True, verbose_name='verified at')),
            ],
        ),
    ]