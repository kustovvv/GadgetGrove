# Generated by Django 4.2.5 on 2023-10-29 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0029_delete_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCompare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_items', models.ManyToManyField(to='item.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]