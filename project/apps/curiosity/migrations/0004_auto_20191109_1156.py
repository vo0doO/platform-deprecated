# Generated by Django 2.2.7 on 2019-11-09 08:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('curiosity', '0003_auto_20191109_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.UUIDField(default=uuid.UUID('05711b2c-86ae-434c-8948-1dd51bae21d6'), primary_key=True, serialize=False, verbose_name='Интификатор'),
        ),
    ]
