# Generated by Django 5.0.6 on 2024-05-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_product_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='info', verbose_name='img info')),
                ('name', models.CharField(max_length=50, verbose_name='name imfo')),
                ('text', models.TextField(verbose_name='text info')),
                ('price', models.IntegerField(verbose_name='Price')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='cat',
        ),
        migrations.DeleteModel(
            name='cat',
        ),
    ]
