# Generated by Django 4.1.3 on 2022-11-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Url Slug'),
        ),
    ]
