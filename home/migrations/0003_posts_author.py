# Generated by Django 4.1.2 on 2022-10-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_posts_category_posts_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
