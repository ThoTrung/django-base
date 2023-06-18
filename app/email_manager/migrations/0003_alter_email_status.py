# Generated by Django 4.0.10 on 2023-06-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_manager', '0002_alter_email_cancel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='status',
            field=models.CharField(choices=[('NEW', 'Tài khoản mới'), ('WORKING', 'Tài khoản đang dùng'), ('CANCELED', 'Tài khoản đã bị xóa')], default='WORKING', max_length=20),
        ),
    ]
