# Generated by Django 2.2.3 on 2019-07-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('males', '0005_auto_20180221_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=40)),
                ('text', models.TextField()),
            ],
        ),
    ]