# Generated by Django 5.1 on 2024-08-25 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app', '0002_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
