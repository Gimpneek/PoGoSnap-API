# Generated by Django 2.0.3 on 2018-04-12 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_pokedexentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokedex',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'entries',
                    models.ManyToManyField(blank=True, to='api.PokedexEntry')),
                (
                    'profile',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to='api.Profile'
                    )
                ),
            ],
        ),
    ]
