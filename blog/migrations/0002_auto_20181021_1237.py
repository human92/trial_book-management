# Generated by Django 2.1 on 2018-10-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
