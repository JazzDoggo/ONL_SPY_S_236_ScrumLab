# Generated by Django 5.0.2 on 2024-03-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0002_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
