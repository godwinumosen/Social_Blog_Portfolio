# Generated by Django 4.1.4 on 2023-07-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blogmode_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmode',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
