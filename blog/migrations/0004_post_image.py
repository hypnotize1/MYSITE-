# Generated by Django 5.0.1 on 2024-01-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog-images/default.jpg', upload_to='blog-images/'),
        ),
    ]