# Generated by Django 3.2.7 on 2021-09-23 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReserchLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='semsy',
            options={'ordering': ['sy', 'sem']},
        ),
    ]
