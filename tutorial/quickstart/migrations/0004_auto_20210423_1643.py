# Generated by Django 3.2 on 2021-04-23 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0003_followers_followed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='followers',
            name='follows',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
