# Generated by Django 4.0.6 on 2022-08-02 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0006_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, default='LibreriaCoderApp\\static\\LibreriaCoderApp\x07ssets\\img\\AvatarPorDefecto.png', null=True, upload_to='blog'),
        ),
    ]
