# Generated by Django 4.2.16 on 2024-09-30 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_favourite_added_on_alter_post_added_on_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='added_on',
        ),
        migrations.AlterField(
            model_name='favourite',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
