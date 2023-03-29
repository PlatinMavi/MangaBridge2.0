# Generated by Django 4.0.6 on 2023-03-28 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manga', '0014_alter_categorys_options_alter_manga_options_and_more'),
        ('Users', '0004_rename_pp_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bookmarks',
            field=models.ManyToManyField(to='Manga.manga'),
        ),
    ]