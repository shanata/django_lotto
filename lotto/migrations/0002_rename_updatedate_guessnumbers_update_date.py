# Generated by Django 3.2 on 2022-05-12 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guessnumbers',
            old_name='updatedate',
            new_name='update_date',
        ),
    ]
