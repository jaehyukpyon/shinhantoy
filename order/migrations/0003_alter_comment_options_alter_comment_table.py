# Generated by Django 4.1.5 on 2023-01-26 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '주문의 댓글', 'verbose_name_plural': '주문의 댓글(들)'},
        ),
        migrations.AlterModelTable(
            name='comment',
            table='shinhan_order_comment',
        ),
    ]