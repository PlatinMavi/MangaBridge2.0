# Generated by Django 4.0.6 on 2023-01-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manga', '0003_manga_manga_image_alter_chapter_chapter_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='manga_image',
            field=models.ImageField(default='noimage.png', upload_to='thumbnail'),
        ),
    ]
