# Generated by Django 4.0.3 on 2022-04-09 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_alter_room_options_room_host_message_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='category',
            new_name='topic',
        ),
    ]