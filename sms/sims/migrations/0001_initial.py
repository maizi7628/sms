# Generated by Django 4.2.14 on 2024-09-14 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_no', models.CharField(max_length=32, unique=True)),
                ('student_name', models.CharField(max_length=32)),
            ],
        ),
    ]
