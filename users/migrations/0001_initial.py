# Generated by Django 3.2.4 on 2021-06-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SortUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='user level')),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], default='MALE', max_length=7, verbose_name='gender')),
                ('age', models.PositiveIntegerField(default=18, max_length=3)),
                ('english_level', models.CharField(choices=[('1', 'A1'), ('2', 'A2'), ('3', 'B1'), ('4', 'B2'), ('5', 'C1')], max_length=20, verbose_name='English level')),
            ],
        ),
    ]
