# Generated by Django 4.1.1 on 2023-04-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='About',
            field=models.CharField(max_length=200, null=True),
        ),
    ]