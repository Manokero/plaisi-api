# Generated by Django 2.2.3 on 2019-07-21 15:48

import apps.proprietary.helpers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proprietary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField(blank=True, null=True)),
                ('province', models.CharField(choices=[('SD', 'Santo Domingo'), ('SC', 'San Cristobal'), ('SA', 'Santiago')], default='SD', max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProprietaryLegalDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to=apps.proprietary.helpers.proprietary_legal_documents_path)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('proprietary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proprietary.Proprietary')),
            ],
        ),
    ]