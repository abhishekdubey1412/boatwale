# Generated by Django 5.0.3 on 2024-04-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_tourimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='price',
            new_name='new_price',
        ),
        migrations.AddField(
            model_name='tour',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='tourimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tours-packages/'),
        ),
    ]
