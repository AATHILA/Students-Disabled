# Generated by Django 4.2.5 on 2024-01-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0075_alter_questionaudio_type_alter_questionimages_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]