# Generated by Django 4.2.3 on 2023-08-07 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_s_school_student_previous_school_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
