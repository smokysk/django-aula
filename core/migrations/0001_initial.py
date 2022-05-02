# Generated by Django 4.0.4 on 2022-04-22 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'city',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('abbreviation', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'state',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'zone',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
                ('city', models.ForeignKey(db_column='id_city', on_delete=django.db.models.deletion.DO_NOTHING, to='core.city')),
                ('zone', models.ForeignKey(db_column='id_zone', on_delete=django.db.models.deletion.DO_NOTHING, to='core.zone')),
            ],
            options={
                'db_table': 'district',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(db_column='id_state', on_delete=django.db.models.deletion.DO_NOTHING, to='core.state'),
        ),
    ]