# Generated by Django 5.0.3 on 2024-04-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='react',
            name='dislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='react',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
