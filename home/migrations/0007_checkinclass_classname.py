# Generated by Django 3.0.6 on 2020-06-01 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200602_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkinclass',
            name='classname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Classname'),
        ),
    ]
