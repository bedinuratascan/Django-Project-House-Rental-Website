# Generated by Django 3.0.3 on 2020-05-14 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_faq_ordernr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='ordernr',
            new_name='orderNumber',
        ),
    ]
