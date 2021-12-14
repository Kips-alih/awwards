# Generated by Django 2.2.24 on 2021-12-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsapp', '0006_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='content_rating',
            new_name='content_rate',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='design_rating',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='usability_rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='design_rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='usability_rate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]