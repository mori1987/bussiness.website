# Generated by Django 5.0.2 on 2024-03-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_description_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='mori', max_length=200),
        ),
    ]