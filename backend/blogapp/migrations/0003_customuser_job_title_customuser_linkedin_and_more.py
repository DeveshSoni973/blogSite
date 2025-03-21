# Generated by Django 5.1.2 on 2024-11-16 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='job_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='linkedin',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fullstack', 'Fullstack'), ('Design', 'Design'), ('Blockchain', 'Blockchain')], max_length=255, null=True),
        ),
    ]
