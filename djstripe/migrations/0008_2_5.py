# Generated by Django 3.2.3 on 2021-05-30 23:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):
    dependencies = [
        ("djstripe", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscription",
            name="tax_percent",
        ),
        migrations.RemoveField(
            model_name="countryspec",
            name="djstripe_owner_account",
        ),
        migrations.AddField(
            model_name="card",
            name="account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The external account the charge was made on behalf of. Null here indicates that this value was never set.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="cards",
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="card",
            name="default_for_currency",
            field=models.BooleanField(
                help_text="Whether this external account (Card) is the default account for its currency.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="bankaccount",
            name="account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The external account the charge was made on behalf of. Null here indicates that this value was never set.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="bank_accounts",
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AlterField(
            model_name="bankaccount",
            name="default_for_currency",
            field=models.BooleanField(
                help_text="Whether this external account (BankAccount) is the default account for its currency.",
                null=True,
            ),
        ),
        migrations.RenameModel(
            old_name="FileUpload",
            new_name="File",
        ),
        migrations.CreateModel(
            name="FileLink",
            fields=[
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The datetime this object was created in stripe.",
                        null=True,
                    ),
                ),
                (
                    "metadata",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A description of this object.", null=True
                    ),
                ),
                (
                    "expires_at",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="Time at which the link expires.",
                        null=True,
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        help_text="The publicly accessible URL to download the file."
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The Stripe Account this object belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "file",
                    djstripe.fields.StripeForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.file",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Mandate",
            fields=[
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The datetime this object was created in stripe.",
                        null=True,
                    ),
                ),
                (
                    "metadata",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A description of this object.", null=True
                    ),
                ),
                (
                    "customer_acceptance",
                    djstripe.fields.JSONField(
                        help_text="Details about the customer's acceptance of the mandate."
                    ),
                ),
                (
                    "payment_method_details",
                    djstripe.fields.JSONField(
                        help_text="Additional mandate information specific to the payment method type."
                    ),
                ),
                (
                    "status",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.MandateStatus,
                        help_text="The status of the mandate, which indicates whether it can be used to initiate a payment.",
                        max_length=8,
                    ),
                ),
                (
                    "type",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.MandateType,
                        help_text="The status of the mandate, which indicates whether it can be used to initiate a payment.",
                        max_length=10,
                    ),
                ),
                (
                    "multi_use",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="If this is a `multi_use` mandate, this hash contains details about the mandate.",
                        null=True,
                    ),
                ),
                (
                    "single_use",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="If this is a `single_use` mandate, this hash contains details about the mandate.",
                        null=True,
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The Stripe Account this object belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "payment_method",
                    djstripe.fields.StripeForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.paymentmethod",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="charge",
            name="source",
            field=djstripe.fields.PaymentMethodForeignKey(
                blank=True,
                help_text="The source used for this charge.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="charges",
                to="djstripe.djstripepaymentmethod",
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="default_source",
            field=djstripe.fields.PaymentMethodForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="customers",
                to="djstripe.djstripepaymentmethod",
            ),
        ),
    ]
