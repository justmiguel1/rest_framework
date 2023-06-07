# Generated by Django 4.2.1 on 2023-06-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Продукты '},
        ),
        migrations.AddField(
            model_name='products',
            name='descriptions_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='products',
            name='descriptions_ru',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='products',
            name='gender_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='products',
            name='gender_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='products',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='products',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=50, verbose_name='Username'),
        ),
    ]
