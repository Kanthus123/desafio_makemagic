# Generated by Django 3.1.2 on 2020-11-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personagensapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personagem',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Identidade',
        ),
    ]
