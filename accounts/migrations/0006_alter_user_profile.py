# Generated by Django 5.0.1 on 2024-01-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True),
        ),
    ]