# Generated by Django 4.1.2 on 2022-10-26 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('sent_by', models.CharField(max_length=300)),
                ('received_by', models.CharField(max_length=300)),
            ],
        ),
    ]
