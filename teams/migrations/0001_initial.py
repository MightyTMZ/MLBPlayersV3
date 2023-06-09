# Generated by Django 4.1.7 on 2023-03-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('league', models.CharField(choices=[('AL', 'AL'), ('NL', 'NL')], default='--', max_length=255)),
                ('division', models.CharField(choices=[('AL East', 'AL East'), ('AL Central', 'AL Central'), ('AL West', 'AL West'), ('NL East', 'NL East'), ('NL Central', 'NL Central'), ('NL West', 'NL West')], default='--', max_length=255)),
                ('img_url', models.ImageField(upload_to='teams/media/images')),
                ('identification', models.CharField(max_length=255)),
            ],
        ),
    ]
