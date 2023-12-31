# Generated by Django 4.1.11 on 2023-09-24 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_title', models.CharField(max_length=100)),
                ('skills_used', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('github_link', models.URLField(blank=True)),
            ],
        ),
    ]
