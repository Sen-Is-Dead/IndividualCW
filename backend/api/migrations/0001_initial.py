# Generated by Django 4.2.5 on 2023-11-07 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(max_length=100)),
                ('date_field', models.DateField()),
                ('email_field', models.EmailField(max_length=254)),
                ('integer_field', models.IntegerField()),
            ],
        ),
    ]
