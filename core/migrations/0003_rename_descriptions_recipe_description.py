# Generated by Django 4.0.6 on 2022-10-02 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='descriptions',
            new_name='description',
        ),
    ]
