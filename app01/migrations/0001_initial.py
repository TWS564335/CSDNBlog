# Generated by Django 2.0.4 on 2018-06-26 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pub_date', models.DateField()),
                ('publish', models.CharField(max_length=32)),
            ],
        ),
    ]
