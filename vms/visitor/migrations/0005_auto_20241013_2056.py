# Generated by Django 3.2.25 on 2024-10-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0004_alter_visitor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='visitor_images'),
        ),
    ]
