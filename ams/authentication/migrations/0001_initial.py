# Generated by Django 4.1.3 on 2023-05-17 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
