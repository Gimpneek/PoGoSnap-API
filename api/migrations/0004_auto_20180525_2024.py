# Generated by Django 2.0.5 on 2018-05-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_profile_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(
                help_text='Name of the user',
                max_length=128,
                unique=True
            ),
        ),
    ]
