# Generated by Django 3.1.4 on 2020-12-09 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_name',
            name='age',
            field=models.TextField(),
        ),
    ]
