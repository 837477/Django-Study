# Generated by Django 4.0.4 on 2022-05-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='updated_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
