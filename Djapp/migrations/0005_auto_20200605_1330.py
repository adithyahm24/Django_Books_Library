# Generated by Django 3.0.3 on 2020-06-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Djapp', '0004_auto_20200605_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='date',
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]