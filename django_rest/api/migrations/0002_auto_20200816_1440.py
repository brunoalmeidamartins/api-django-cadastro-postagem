# Generated by Django 3.1 on 2020-08-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='url_imagem',
            field=models.CharField(max_length=300),
        ),
    ]