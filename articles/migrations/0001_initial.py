# Generated by Django 4.0 on 2021-12-18 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('summary', models.CharField(blank=True, max_length=200)),
                ('body', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.customuser')),
            ],
        ),
    ]
