# Generated by Django 4.0.2 on 2022-02-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zip',
            name='zip',
            field=models.IntegerField(default=411044),
            preserve_default=False,
        ),
    ]