# Generated by Django 4.0.6 on 2023-01-30 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manga', '0004_alter_manga_manga_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='manga_image',
            field=models.ImageField(default='thumbnail/noimage.png', upload_to='thumbnail'),
        ),
    ]
