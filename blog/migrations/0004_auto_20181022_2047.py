# Generated by Django 2.1 on 2018-10-22 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181021_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=50)),
                ('img', models.BinaryField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='imag_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.BookImage'),
        ),
    ]
