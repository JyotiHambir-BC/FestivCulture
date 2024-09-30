# Generated by Django 4.2.16 on 2024-09-30 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_post_added_on_alter_favourite_added_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
