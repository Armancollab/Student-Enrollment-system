# Generated by Django 4.2.3 on 2023-08-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='s_school',
            new_name='previous_school',
        ),
        migrations.RemoveField(
            model_name='student',
            name='s_email',
        ),
        migrations.AddField(
            model_name='student',
            name='s_phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]
