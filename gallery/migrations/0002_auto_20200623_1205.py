# Generated by Django 3.0.7 on 2020-06-23 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='作品的标题', max_length=20),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='作品的描述', max_length=100),
        ),
    ]
