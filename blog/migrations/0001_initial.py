# Generated by Django 3.0.3 on 2020-02-15 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('body', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
