# Generated by Django 4.0.10 on 2023-06-28 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_manager', '0003_alter_email_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='status',
            field=models.CharField(choices=[['NEW', 'Tài khoản mới'], ['PENDING', 'Tài khoản đang bị pending'], ['WORKING', 'Tài khoản đang dùng'], ['CANCELING', 'Tài khoản đang bị xóa'], ['CANCELED', 'Tài khoản đã bị xóa']], default='WORKING', max_length=20),
        ),
    ]
