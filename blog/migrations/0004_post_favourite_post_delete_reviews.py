# Generated by Django 4.2.16 on 2024-09-25 10:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favourite_post',
            field=models.ManyToManyField(blank=True, related_name='favourite_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
