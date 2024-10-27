# Generated by Django 5.0.6 on 2024-07-15 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blog_image_blog_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=1, upload_to='blog/'),
            preserve_default=False,
        ),
    ]