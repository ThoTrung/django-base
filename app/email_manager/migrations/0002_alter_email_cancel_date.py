# Generated by Django 4.0.10 on 2023-06-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='cancel_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
