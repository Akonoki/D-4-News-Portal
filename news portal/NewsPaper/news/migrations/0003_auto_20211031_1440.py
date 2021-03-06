# Generated by Django 3.2.8 on 2021-10-31 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20211016_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=256, verbose_name='заглавие'),
        ),
    ]
