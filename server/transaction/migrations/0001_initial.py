# Generated by Django 4.2.4 on 2023-09-29 09:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionGroup',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('balance', models.IntegerField(default=0)),
                ('expenses', models.IntegerField(default=0)),
                ('income', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_auth.googleuser')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transactiongroup')),
            ],
        ),
    ]
