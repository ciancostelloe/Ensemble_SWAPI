# Generated by Django 2.2.3 on 2019-07-12 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('height', models.CharField(blank=True, max_length=10)),
                ('mass', models.CharField(blank=True, max_length=10)),
                ('hair_color', models.CharField(blank=True, max_length=20)),
                ('skin_color', models.CharField(blank=True, max_length=20)),
                ('eye_color', models.CharField(blank=True, max_length=20)),
                ('birth_year', models.CharField(blank=True, max_length=10)),
                ('gender', models.CharField(blank=True, max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('rotation_period', models.CharField(max_length=40)),
                ('orbital_period', models.CharField(max_length=40)),
                ('diameter', models.CharField(max_length=40)),
                ('climate', models.CharField(max_length=40)),
                ('gravity', models.CharField(max_length=40)),
                ('terrain', models.CharField(max_length=40)),
                ('surface_water', models.CharField(max_length=40)),
                ('population', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=40)),
                ('manufacturer', models.CharField(max_length=80)),
                ('cost_in_credits', models.CharField(max_length=40)),
                ('length', models.CharField(max_length=40)),
                ('max_atmosphering_speed', models.CharField(max_length=40)),
                ('crew', models.CharField(max_length=40)),
                ('passengers', models.CharField(max_length=40)),
                ('cargo_capacity', models.CharField(max_length=40)),
                ('consumables', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('classification', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=40)),
                ('average_height', models.CharField(max_length=40)),
                ('skin_colors', models.CharField(max_length=200)),
                ('hair_colors', models.CharField(max_length=200)),
                ('eye_colors', models.CharField(max_length=200)),
                ('average_lifespan', models.CharField(max_length=40)),
                ('language', models.CharField(max_length=40)),
                ('homeworld', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chewy.Planet')),
                ('people', models.ManyToManyField(related_name='species', to='chewy.People')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to='chewy.Planet'),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('transport_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chewy.Transport')),
                ('vehicle_class', models.CharField(max_length=40)),
                ('pilots', models.ManyToManyField(blank=True, related_name='vehicles', to='chewy.People')),
            ],
            options={
                'abstract': False,
            },
            bases=('chewy.transport',),
        ),
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('transport_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chewy.Transport')),
                ('hyperdrive_rating', models.CharField(max_length=40)),
                ('MGLT', models.CharField(max_length=40)),
                ('starship_class', models.CharField(max_length=40)),
                ('pilots', models.ManyToManyField(blank=True, related_name='starships', to='chewy.People')),
            ],
            options={
                'abstract': False,
            },
            bases=('chewy.transport',),
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('episode_id', models.IntegerField()),
                ('opening_crawl', models.TextField(max_length=1000)),
                ('director', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('characters', models.ManyToManyField(blank=True, related_name='films', to='chewy.People')),
                ('planets', models.ManyToManyField(blank=True, related_name='films', to='chewy.Planet')),
                ('species', models.ManyToManyField(blank=True, related_name='films', to='chewy.Species')),
                ('starships', models.ManyToManyField(blank=True, related_name='films', to='chewy.Starship')),
                ('vehicles', models.ManyToManyField(blank=True, related_name='films', to='chewy.Vehicle')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
