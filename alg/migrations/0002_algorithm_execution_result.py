# Generated by Django 3.0.4 on 2020-03-12 08:40

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm_execution_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.DecimalField(decimal_places=8, max_digits=15)),
                ('input_mas', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('result_mas', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('name_alg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alg.Alg')),
            ],
        ),
    ]
