# Generated by Django 3.1.7 on 2021-03-26 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_tag_priority_rank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('priority_rank',)},
        ),
    ]