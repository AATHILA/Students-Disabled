# Generated by Django 4.2.5 on 2024-01-10 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0076_student_email'),
        ('home', '0007_alter_notes_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.category'),
        ),
    ]
