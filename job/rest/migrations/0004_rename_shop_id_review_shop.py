# Generated by Django 4.1.1 on 2023-04-20 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='shop_id',
            new_name='shop',
        ),
    ]