# Generated by Django 3.0.5 on 2020-05-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200504_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye fotoğraf ekleyin'),
        ),
    ]
