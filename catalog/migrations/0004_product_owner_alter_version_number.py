# Generated by Django 4.2.7 on 2024-01-03 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_alter_contact_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='продавец'),
        ),
        migrations.AlterField(
            model_name='version',
            name='number',
            field=models.CharField(max_length=8, verbose_name='Номер версии'),
        ),
    ]
