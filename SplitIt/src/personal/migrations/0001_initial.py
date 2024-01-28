# Generated by Django 5.0.1 on 2024-01-27 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('quesiton', models.TextField(max_length=300)),
                ('priority', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], max_length=1)),
            ],
        ),
    ]
