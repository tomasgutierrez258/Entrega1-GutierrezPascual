# Generated by Django 4.1.2 on 2022-10-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_posts_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='edited',
            field=models.BooleanField(default=False),
        ),
    ]