# Generated by Django 4.0.6 on 2022-08-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_masdatosusuarios_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masdatosusuarios',
            name='avatar',
            field=models.ImageField(blank=True, default='LibreriaCoderApp/assets/img/AvatarPorDefecto.png', null=True, upload_to='avatares'),
        ),
    ]
