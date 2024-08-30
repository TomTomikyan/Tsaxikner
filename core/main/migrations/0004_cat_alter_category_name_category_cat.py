# Generated by Django 5.0.6 on 2024-05-17 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_category_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='cat name')),
                ('img', models.ImageField(null=True, upload_to='cat/', verbose_name='cat img')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Cat name'),
        ),
        migrations.AddField(
            model_name='category',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='main.cat'),
        ),
    ]
