# Generated by Django 4.0.6 on 2023-03-23 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manga', '0011_rename_duyuru_description_duyuru_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='manga_description',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]
