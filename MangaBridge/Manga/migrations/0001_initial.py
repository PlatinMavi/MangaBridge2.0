# Generated by Django 4.0.6 on 2023-01-28 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fansub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fansub_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manga_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fansub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manga.fansub')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manga.manga')),
            ],
        ),
    ]
