# Generated by Django 3.0.8 on 2020-07-08 22:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200708_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='html_content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]