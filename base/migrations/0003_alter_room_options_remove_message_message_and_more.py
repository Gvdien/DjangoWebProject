# Generated by Django 4.1.1 on 2022-09-18 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='body',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
