# Generated by Django 4.2.3 on 2023-09-01 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('SchName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('SchPricipal', models.CharField(max_length=100)),
                ('SchLocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuName', models.CharField(max_length=100)),
                ('StuId', models.IntegerField(max_length=100)),
                ('SchName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
    ]
