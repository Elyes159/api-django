# Generated by Django 4.2.10 on 2024-03-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompteSnapchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_compte', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('followers', models.IntegerField()),
            ],
        ),
    ]
