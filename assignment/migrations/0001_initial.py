# Generated by Django 4.2.1 on 2023-05-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='It store the company_name', max_length=250)),
                ('city', models.CharField(help_text='It store the city in which company is establised', max_length=100)),
                ('is_active', models.BooleanField(default=True, help_text='it tells that company still exist/active')),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]
