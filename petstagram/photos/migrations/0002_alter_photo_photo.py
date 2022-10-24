# Generated by Django 4.1.2 on 2022-10-19 13:21

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='images', validators=[petstagram.photos.validators.validate_image_size]),
        ),
    ]