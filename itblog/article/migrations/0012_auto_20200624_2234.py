# Generated by Django 3.0.6 on 2020-06-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20200624_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='article', to='article.Tag'),
        ),
    ]