# Generated by Django 5.0.7 on 2024-07-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='player_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
