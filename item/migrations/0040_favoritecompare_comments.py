# Generated by Django 4.2.5 on 2023-11-09 17:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0039_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCompare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compare_items', models.ManyToManyField(related_name='compares', to='item.item')),
                ('favorite_items', models.ManyToManyField(related_name='favorites', to='item.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_compares', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('comment', models.TextField()),
                ('advantages', models.CharField(blank=True, max_length=255, null=True)),
                ('disadvantages', models.CharField(blank=True, max_length=255, null=True)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='item.item')),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'ordering': ('-comment_date',),
            },
        ),
    ]
