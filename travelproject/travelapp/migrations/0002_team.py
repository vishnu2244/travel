# Generated by Django 4.1.2 on 2022-11-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_name', models.CharField(max_length=200)),
                ('T_img', models.ImageField(upload_to='pics')),
                ('T_desc', models.TextField()),
            ],
        ),
    ]
