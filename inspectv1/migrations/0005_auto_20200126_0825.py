# Generated by Django 3.0.2 on 2020-01-26 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspectv1', '0004_auto_20200126_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemincategory',
            name='throw_error',
            field=models.BooleanField(verbose_name='Throw error if True'),
        ),
    ]
