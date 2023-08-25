# Generated by Django 4.2.2 on 2023-08-07 13:23

from django.db import migrations, models

import care.utils.models.validators


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0375_alter_dailyround_resp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ambulance",
            name="owner_phone_number",
            field=models.CharField(
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="ambulancedriver",
            name="phone_number",
            field=models.CharField(
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="asset",
            name="support_phone",
            field=models.CharField(
                default="",
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline", "support")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="facility",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatientregistration",
            name="emergency_phone_number",
            field=models.CharField(
                default="",
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="historicalpatientregistration",
            name="phone_number",
            field=models.CharField(
                default="",
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="patientmobileotp",
            name="phone_number",
            field=models.CharField(
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="patientregistration",
            name="emergency_phone_number",
            field=models.CharField(
                default="",
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="patientregistration",
            name="phone_number",
            field=models.CharField(
                default="",
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="resourcerequest",
            name="refering_facility_contact_number",
            field=models.CharField(
                blank=True,
                default="",
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="shiftingrequest",
            name="ambulance_phone_number",
            field=models.CharField(
                blank=True,
                default="",
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="shiftingrequest",
            name="refering_facility_contact_number",
            field=models.CharField(
                blank=True,
                default="",
                max_length=14,
                validators=[
                    care.utils.models.validators.PhoneNumberValidator(
                        types=("mobile", "landline")
                    )
                ],
            ),
        ),
    ]