# Generated by Django 3.2.15 on 2022-09-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0005_auto_20220822_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing',
            name='brand',
            field=models.TextField(choices=[('Apple', 'Apple'), ('HP', 'HP'), ('Acer', 'Acer'), ('Asus', 'Asus'), ('Dell', 'Dell'), ('Lenovo', 'Lenovo'), ('MSI', 'MSI'), ('Microsoft', 'Microsoft'), ('NotePad', 'NotePad'), ('Toshiba', 'Toshiba'), ('Google', 'Google'), ('Samsung', 'Samsung')], max_length=100),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='type',
            field=models.TextField(choices=[('Ultrabook', 'Ultrabook'), ('Notebook', 'Notebook'), ('Gaming', 'Gaming'), ('2 in 1', '2 in 1')], max_length=100),
        ),
    ]
