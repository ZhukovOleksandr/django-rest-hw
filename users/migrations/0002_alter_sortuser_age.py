# Generated by Django 3.2.4 on 2021-06-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortuser',
            name='age',
            field=models.PositiveIntegerField(default=18),
        ),
    ]
