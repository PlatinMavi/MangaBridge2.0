# Generated by Django 4.0.6 on 2023-02-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manga', '0006_manga_manga_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='relase_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]