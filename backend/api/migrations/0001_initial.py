# Generated by Django 5.0.6 on 2024-05-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=100, null=True)),
                ('price', models.BigIntegerField()),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.TextField()),
                ('status', models.CharField(choices=[('PAID', 'Paid'), ('UNPAID', 'Unpaid'), ('PENDING', 'Pending'), ('FAILURE', 'Failure')], default='UNPAID', max_length=10)),
                ('order_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
