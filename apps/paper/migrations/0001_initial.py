# Generated by Django 3.2.7 on 2021-09-19 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('is_accepted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_created', to=settings.AUTH_USER_MODEL)),
                ('proponent1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_proponent1', to='account.account')),
                ('proponent2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_proponent2', to='account.account')),
                ('proponent3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_proponent3', to='account.account')),
            ],
        ),
    ]
