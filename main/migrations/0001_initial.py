# Generated by Django 4.2 on 2023-04-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Названиетупа')),
                ('task', models.TextField(verbose_name='Описаниетупа')),
            ],
        ),
    ]
