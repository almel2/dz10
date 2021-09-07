# Generated by Django 3.2.7 on 2021-09-07 11:09
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RemoveField(
            model_name='provider',
            name='id',
        ),
        migrations.AlterField(
            model_name='provider',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.city'),
        ),
    ]