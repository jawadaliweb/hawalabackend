# Generated by Django 4.1.3 on 2022-11-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=0)),
                ('receive', models.IntegerField(default=0)),
                ('payment', models.IntegerField(default=0)),
            ],
        ),
    ]
