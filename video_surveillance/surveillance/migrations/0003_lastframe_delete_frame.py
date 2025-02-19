# Generated by Django 5.1.3 on 2024-11-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveillance', '0002_frame_delete_videoframe'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame', models.BinaryField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Frame',
        ),
    ]
