# Generated by Django 4.0.4 on 2022-04-23 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_food_type_foof_alter_food_price_alter_food_rate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='type_foof',
            new_name='type_food',
        ),
    ]