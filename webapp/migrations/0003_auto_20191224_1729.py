# Generated by Django 3.0.1 on 2019-12-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191224_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='early_repayment',
            field=models.BooleanField(default=False, verbose_name='early repayment'),
        ),
    ]
