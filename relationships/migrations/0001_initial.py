# Generated by Django 4.0.6 on 2022-09-25 01:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='タイトル')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='価格')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日付')),
            ],
            options={
                'db_table': 'Book',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'Place',
                'ordering': ['name'],
            },
        ),
    ]
