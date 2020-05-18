# Generated by Django 3.0.6 on 2020-05-18 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('omdb_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=1)),
                ('year', models.SmallIntegerField()),
                ('genre', models.CharField(max_length=32)),
            ],
        ),
    ]
