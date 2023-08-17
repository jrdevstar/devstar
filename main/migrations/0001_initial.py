# Generated by Django 4.1.5 on 2023-02-13 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('unif_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.unif')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('main.unif',),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('unif_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.unif')),
                ('date', models.DateField(auto_now_add=True)),
                ('video', models.URLField(default=None)),
            ],
            bases=('main.unif',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('unif_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.unif')),
                ('used_tech', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('main.unif',),
        ),
    ]
