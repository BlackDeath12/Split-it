# Generated by Django 5.0.1 on 2024-01-27 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'the question', 'verbose_name_plural': "Users's questions"},
        ),
        migrations.AlterField(
            model_name='question',
            name='quesiton',
            field=models.TextField(max_length=400),
        ),
    ]