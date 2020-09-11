# Generated by Django 3.0.4 on 2020-09-10 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200911_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('impact_on_society', models.TextField()),
                ('awards', models.TextField(blank=True)),
                ('funds_used', models.FloatField()),
                ('image1', models.ImageField(default='default.png', upload_to='images/')),
                ('image2', models.ImageField(default='default.png', upload_to='images/')),
                ('image3', models.ImageField(default='default.png', upload_to='images/')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Event')),
            ],
        ),
    ]