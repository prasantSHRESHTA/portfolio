# Generated by Django 4.1.11 on 2023-09-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_edu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edu',
            name='field_of_study',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
