# Generated by Django 3.1 on 2020-08-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=6)),
                ('subject_name', models.CharField(max_length=50)),
                ('lecturer', models.CharField(max_length=50)),
                ('room', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=3)),
                ('starttime', models.CharField(max_length=5)),
                ('endtime', models.CharField(max_length=5)),
                ('color', models.CharField(max_length=9)),
            ],
        ),
    ]
