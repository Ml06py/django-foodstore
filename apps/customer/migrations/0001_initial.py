# Generated by Django 4.0.4 on 2022-07-10 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0004_food_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(blank=True, max_length=15)),
                ('total_price', models.IntegerField(blank=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ordered', 'Ordered'), ('preparing', 'Preparing'), ('sending', 'Sending'), ('Arrived', 'Arrived')], default='ordered', max_length=10)),
                ('items', models.ManyToManyField(blank=True, to='restaurant.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
