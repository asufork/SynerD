# Generated by Django 3.0.4 on 2020-04-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('middle', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('dobday', models.CharField(max_length=200)),
                ('dobmonth', models.CharField(max_length=200)),
                ('dobyear', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('homephone', models.CharField(max_length=200)),
                ('cell', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('employername', models.CharField(max_length=200)),
                ('employeraddress1', models.CharField(max_length=200)),
                ('employeraddress2', models.CharField(max_length=200)),
                ('employercity', models.CharField(max_length=200)),
                ('employerzip', models.CharField(max_length=200)),
                ('employerphone', models.CharField(max_length=200)),
                ('jobtitle', models.CharField(max_length=200)),
                ('governmentIDtype', models.CharField(max_length=200)),
                ('governmentIDnumber', models.CharField(max_length=200)),
                ('governmentIDissuecountry', models.CharField(max_length=200)),
                ('governmentIDissuestate', models.CharField(max_length=200)),
                ('governmentIDissue', models.CharField(max_length=200)),
                ('governmentIDexpiredate', models.DateField()),
                ('beneficiaryID', models.CharField(max_length=200)),
            ],
        ),
    ]
