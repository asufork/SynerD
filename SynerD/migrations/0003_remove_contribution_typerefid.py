# Generated by Django 3.0.4 on 2020-04-06 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SynerD', '0002_contribution_event_fee_office_officer_organization_organizationmember_payment_service_subscriber_sub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contribution',
            name='typerefID',
        ),
    ]