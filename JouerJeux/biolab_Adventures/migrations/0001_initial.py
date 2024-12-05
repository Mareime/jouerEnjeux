# Generated by Django 5.1.3 on 2024-12-05 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('niveau', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1)),
                ('test_question', models.TextField()),
                ('choix1', models.CharField(max_length=255)),
                ('choix2', models.CharField(max_length=255)),
                ('choix3', models.CharField(max_length=255)),
                ('reponse_correct', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mot_de_passe', models.CharField(max_length=255)),
                ('score', models.IntegerField(default=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('choix_correct', models.CharField(max_length=255)),
                ('reponse_choisie', models.CharField(max_length=255)),
                ('id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biolab_Adventures.question')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biolab_Adventures.user')),
            ],
        ),
    ]