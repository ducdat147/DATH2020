# Generated by Django 3.0.6 on 2020-06-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_checkinclass_classname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinclass',
            name='classname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tên lớp'),
        ),
    ]
