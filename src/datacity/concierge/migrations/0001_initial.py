# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conjunto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('administrador', models.IntegerField(default=0, null=True)),
                ('estatus', models.IntegerField(default=0, null=True)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=25)),
                ('pais', models.CharField(max_length=15)),
                ('cp', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NuevoConjunto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('estatus', models.IntegerField(default=0, null=True)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=25)),
                ('pais', models.CharField(max_length=15)),
                ('cp', models.CharField(max_length=10)),
                ('conjunto_creado', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NuevoUsuario',
            fields=[
                ('id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('pertenece_conjunto', models.ForeignKey(to='concierge.Conjunto')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('passwd', models.CharField(max_length=128, null=True)),
                ('pertenece_conjunto', models.IntegerField(default=0, null=True)),
                ('estatus', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='nuevoconjunto',
            name='administrador',
            field=models.ForeignKey(to='concierge.Usuario'),
        ),
    ]
