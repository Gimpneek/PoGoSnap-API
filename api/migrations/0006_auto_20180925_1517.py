# Generated by Django 2.0.7 on 2018-09-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180526_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(default='Pokedex', max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='pokedex',
            name='entries',
        ),
        migrations.RemoveField(
            model_name='pokedex',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='pokedexentry',
            name='pokemon',
        ),
        migrations.DeleteModel(
            name='Pokedex',
        ),
        migrations.AddField(
            model_name='collection',
            name='entries',
            field=models.ManyToManyField(blank=True, to='api.PokedexEntry'),
        ),
        migrations.AddField(
            model_name='collection',
            name='profile',
            field=models.ManyToManyField(to='api.Profile'),
        ),
    ]
