# Generated by Django 4.1.7 on 2023-03-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField()),
                ('price_per_liter', models.FloatField()),
                ('total_value', models.FloatField()),
            ],
        ),
    ]
