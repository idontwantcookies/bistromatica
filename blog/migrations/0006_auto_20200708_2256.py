# Generated by Django 3.0.8 on 2020-07-08 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='html_content',
            new_name='content',
        ),
    ]