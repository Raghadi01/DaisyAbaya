# Generated by Django 4.2.1 on 2023-05-28 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('massage', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
