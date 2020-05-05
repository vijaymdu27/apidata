# Generated by Django 3.0.5 on 2020-05-05 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiView',
            fields=[
                ('id', models.SlugField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=300)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('company', models.CharField(max_length=500)),
                ('company_url', models.URLField(max_length=100, null=True)),
                ('location', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
    ]
