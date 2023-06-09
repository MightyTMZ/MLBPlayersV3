# Generated by Django 4.1.7 on 2023-03-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arizona_Diamondback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Atlanta_Brave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Baltimore_Oriole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Boston_Red_Sox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Chicago_Cub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Chicago_White_Sox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Cincinnati_Red',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Cleveland_Guardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Colorado_Rockie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Detroit_Tiger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Houston_Astro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Kansas_City_Royal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Los_Angeles_Angel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Los_Angeles_Dodger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Miami_Marlin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Milwaukee_Brewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Minnesota_Twin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='New_York_Met',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='New_York_Yankee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Oakland_Athletic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Philadelphia_Phillie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Pittsburgh_Pirate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='San_Diego_Padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='San_Francisco_Giant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Seattle_Mariner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='St_Louis_Cardinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Tampa_Bay_Ray',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('league', models.CharField(choices=[('AL', 'AL'), ('NL', 'NL')], default='--', max_length=255)),
                ('division', models.CharField(choices=[('AL East', 'AL East'), ('AL Central', 'AL Central'), ('AL West', 'AL West'), ('NL East', 'NL East'), ('NL Central', 'NL Central'), ('NL West', 'NL West')], default='--', max_length=255)),
                ('img_url', models.ImageField(upload_to='media/images')),
            ],
        ),
        migrations.CreateModel(
            name='Texas_Ranger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Toronto_Blue_Jay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Washington_National',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('SP', 'SP'), ('RHP', 'RHP'), ('LHP', 'LHP'), ('1B', '1B'), ('2B', '2B'), ('SS', 'SS'), ('3B', '3B'), ('RF', 'RF'), ('CF', 'CF'), ('LF', 'LF'), ('DH', 'DH'), ('C', 'C')], default='--', max_length=3)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
