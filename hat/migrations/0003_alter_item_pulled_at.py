# Generated by Django 4.1.7 on 2023-04-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hat', '0002_item_pulled_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pulled_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
