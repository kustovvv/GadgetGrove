# Generated by Django 4.2.5 on 2023-10-23 19:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0004_rename_itemrewiew_itemreview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemReview',
            new_name='Review',
        ),
    ]