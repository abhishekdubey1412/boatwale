# Generated by Django 5.0.3 on 2024-04-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='image_alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]