# Generated by Django 3.1.4 on 2020-12-21 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('img', models.CharField(max_length=100)),
            ],
        ),
    ]
