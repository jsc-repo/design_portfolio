# Generated by Django 4.1 on 2022-11-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0006_auto_20160803_0222"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
