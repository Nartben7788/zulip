# Generated by Django 4.2.8 on 2023-12-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("corporate", "0028_zulipsponsorshiprequest_requested_plan"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="tier",
            field=models.SmallIntegerField(null=True),
        ),
    ]
