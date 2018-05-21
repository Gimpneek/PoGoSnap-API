# Generated by Django 2.0.5 on 2018-05-21 20:40

import api.models.image
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
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
                    'image',
                    models.FileField(
                        default=None,
                        upload_to=api.models.image.get_file_path
                    )
                ),
            ],
        ),
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
            ],
        ),
        migrations.CreateModel(
            name='PokedexEntry',
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
                    'image',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to='api.Image'
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
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
                    'name',
                    models.CharField(
                        help_text='Name of the Pokemon',
                        max_length=128
                    )
                ),
                (
                    'dex_number',
                    models.SmallIntegerField(
                        help_text='Number of the Pokemon in the Pokedex'
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
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
                    'name',
                    models.CharField(
                        help_text='Name of the user',
                        max_length=128
                    )
                ),
                (
                    'location',
                    models.CharField(
                        help_text='Location of the user',
                        max_length=128
                    )
                ),
                (
                    'silph_card',
                    models.CharField(
                        help_text="URL of User's Silph Card",
                        max_length=128
                    )
                ),
                (
                    'user',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
        ),
        migrations.AddField(
            model_name='pokedexentry',
            name='pokemon',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='api.Pokemon'),
        ),
        migrations.AddField(
            model_name='pokedex',
            name='entries',
            field=models.ManyToManyField(blank=True, to='api.PokedexEntry'),
        ),
        migrations.AddField(
            model_name='pokedex',
            name='profile',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='api.Profile'),
        ),
        migrations.AddField(
            model_name='image',
            name='pokemon',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='api.Pokemon'),
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='api.Profile'),
        ),
    ]
