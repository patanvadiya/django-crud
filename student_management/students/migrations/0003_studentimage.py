# Generated by Django 4.2.20 on 2025-03-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_hobby'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='student_images/')),
            ],
        ),
    ]
