# Generated by Django 3.2.6 on 2021-08-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_basic_version_lobbys'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='guild',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='mode_game',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='type_user',
            field=models.CharField(max_length=50),
        ),
    ]