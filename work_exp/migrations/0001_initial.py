# Generated by Django 3.0.8 on 2020-07-26 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default name', max_length=10)),
                ('position', models.CharField(default='default position', max_length=25)),
                ('description', models.CharField(default='default description', max_length=150)),
                ('start_date', models.CharField(default='start date', max_length=15)),
                ('end_date', models.CharField(default='end date', max_length=15)),
                ('logo', models.FilePathField(default='default', path='/img')),
            ],
        ),
    ]