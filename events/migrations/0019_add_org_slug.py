# Generated by Django 2.0 on 2018-03-22 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_add_common_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.CharField(default='slug_required', max_length=256),
            preserve_default=False,
        ),
    ]