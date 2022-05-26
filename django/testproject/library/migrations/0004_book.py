# Generated by Django 4.0.4 on 2022-05-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('authors', models.ManyToManyField(to='library.author')),
            ],
        ),
    ]