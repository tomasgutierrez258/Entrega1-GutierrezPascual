# Generated by Django 4.1.2 on 2022-10-28 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_posts_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='user_avatar',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]