# Generated by Django 2.0.3 on 2018-12-05 20:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

from django.conf import settings


currency_kwargs = {}

if getattr(settings, 'AVAILABLE_CURRENCIES', None):
    currency_kwargs['choices'] = [(key, key)
                                  for key in settings.AVAILABLE_CURRENCIES]

if getattr(settings, 'AVAILABLE_CURRENCIES_OVERRIDE', None):
    currency_kwargs['choices'] = settings.AVAILABLE_CURRENCIES_OVERRIDE

if getattr(settings, 'DEFAULT_CURRENCY', None):
    currency_kwargs['default'] = settings.DEFAULT_CURRENCY


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (settings.PAYMENTS_BRAINTREE_PAYMENT_MODEL.split(
            '.')[0], '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('waiting', 'Waiting for confirmation'), ('preauth', 'Pre-authorized'), ('confirmed', 'Confirmed'), (
                    'rejected', 'Rejected'), ('refunded', 'Refunded'), ('error', 'Error'), ('input', 'Input')], default='waiting', max_length=10)),
                ('currency', models.CharField(max_length=10, **currency_kwargs)),
                ('primary', models.DecimalField(
                    decimal_places=2, default='0.0', max_digits=9)),
                ('tax', models.DecimalField(
                    decimal_places=2, default='0.0', max_digits=9)),
                ('delivery', models.DecimalField(
                    decimal_places=2, default='0.0', max_digits=9)),
                ('discount', models.DecimalField(
                    decimal_places=2, default='0.0', max_digits=9)),
                ('description', models.TextField(blank=True, default='')),
                ('extra_data', models.TextField(blank=True, default='')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                              related_name='braintree_transaction_records', to=settings.PAYMENTS_BRAINTREE_PAYMENT_MODEL)),
            ],
            options={
                'permissions': (('view', 'Can view transaction records'), ('edit', 'Can edit transaction records')),
            },
        ),
    ]
