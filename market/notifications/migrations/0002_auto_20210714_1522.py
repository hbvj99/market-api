# Generated by Django 3.1.7 on 2021-07-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='entity_type',
            field=models.CharField(choices=[('user', 'user'), ('product', 'product'), ('comment', 'comment')], max_length=150),
        ),
    ]