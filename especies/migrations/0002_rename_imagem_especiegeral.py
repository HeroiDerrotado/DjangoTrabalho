# Generated by Django 4.2.3 on 2023-07-24 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('especies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Imagem',
            new_name='EspecieGeral',
        ),
    ]