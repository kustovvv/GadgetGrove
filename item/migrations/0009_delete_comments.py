# Generated by Django 4.2.5 on 2023-10-25 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
