# Generated by Django 2.1 on 2018-10-30 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181030_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='blog'),
        ),
    ]
