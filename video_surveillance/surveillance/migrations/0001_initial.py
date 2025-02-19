# Generated by Django 5.1.1 on 2024-09-20 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('frame_data', models.BinaryField()),
                ('sensor_id', models.CharField(max_length=100)),
                ('compressed_size', models.IntegerField()),
                ('original_size', models.IntegerField()),
            ],
        ),
    ]
