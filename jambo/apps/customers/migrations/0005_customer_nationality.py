# Generated by Django 4.2.11 on 2024-04-27 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_alter_customercontact_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='nationality',
            field=models.CharField(db_index=True, default='Kenya', max_length=100),
            preserve_default=False,
        ),
    ]
