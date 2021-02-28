# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-30 20:36
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import cl.disclosures.models
import cl.lib.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people_db', '0047_remove_disclosures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('date_raw', models.TextField(blank=True, help_text='Date of judicial agreement.')),
                ('parties_and_terms', models.TextField(blank=True, help_text='Parties and terms of agreement (ex. Board Member NY Ballet)')),
                ('redacted', models.BooleanField(default=False, help_text='Does the agreement row contain redaction(s)?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('creditor_name', models.TextField(blank=True, help_text='Liability/Debt creditor')),
                ('description', models.TextField(blank=True, help_text='Description of the debt')),
                ('value_code', models.CharField(blank=True, choices=[('J', '1 - 15,000'), ('K', '15,001 - 50,000'), ('L', '50,001 - 100,000'), ('M', '100,001 - 250,000'), ('N', '250,001 - 500,000'), ('O', '500,001 - 1,000,000'), ('P1', '1,000,001 - 5,000,000'), ('P2', '5,000,001 - 25,000,000'), ('P3', '25,000,001 - 50,000,000'), ('P4', '50,000,001 - '), ('-1', 'Failed Extraction')], help_text='Form code for the value of the judicial debt.', max_length=5)),
                ('redacted', models.BooleanField(default=False, help_text='Does the debt row contain redaction(s)?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FinancialDisclosure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('year', models.SmallIntegerField(db_index=True, help_text='The year that the disclosure corresponds with')),
                ('download_filepath', models.TextField(help_text='The path to the original file collected on aws. If split tiff, return url for page one of the disclosures')),
                ('filepath', models.FileField(db_index=True, help_text='The filepath to the disclosure normalized to a PDF.', storage=cl.lib.storage.AWSMediaStorage(), upload_to=cl.disclosures.models.pdf_path)),
                ('thumbnail', models.FileField(blank=True, help_text='A thumbnail of the first page of the disclosure form.', null=True, storage=cl.lib.storage.AWSMediaStorage(), upload_to=cl.disclosures.models.thumbnail_path)),
                ('thumbnail_status', models.SmallIntegerField(choices=[(0, 'Thumbnail needed'), (1, 'Thumbnail completed successfully'), (2, 'Unable to generate thumbnail')], default=0, help_text='The status of the thumbnail generation')),
                ('page_count', models.SmallIntegerField(help_text='The number of pages in the disclosure report')),
                ('sha1', models.CharField(blank=True, db_index=True, help_text='SHA1 hash of the generated PDF', max_length=40, unique=True)),
                ('report_type', models.SmallIntegerField(choices=[(-1, 'Unknown Report'), (0, 'Nomination Report'), (1, 'Initial Report'), (2, 'Annual Report'), (3, 'Final Report')], default=-1, help_text='Financial Disclosure report type')),
                ('is_amended', models.BooleanField(default=False, null=True, help_text='Is disclosure amended?')),
                ('addendum_content_raw', models.TextField(blank=True, help_text='Raw content of addendum with whitespace preserved.')),
                ('addendum_redacted', models.BooleanField(default=False, help_text='Is the addendum partially or completely redacted?')),
                ('has_been_extracted', models.BooleanField(default=False, help_text='Have we successfully extracted the data from PDF?')),
                ('person', models.ForeignKey(help_text='The person that the document is associated with.', on_delete=django.db.models.deletion.CASCADE, related_name='financial_disclosures', to='people_db.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('source', models.TextField(blank=True, help_text='Source of the judicial gift. (ex. Alta Ski Area).')),
                ('description', models.TextField(blank=True, help_text='Description of the gift (ex. Season Pass).')),
                ('value', models.TextField(blank=True, help_text='Value of the judicial gift, (ex. $1,199.00)')),
                ('redacted', models.BooleanField(default=False, help_text='Does the gift row contain redaction(s)?')),
                ('financial_disclosure', models.ForeignKey(help_text='The financial disclosure associated with this gift.', on_delete=django.db.models.deletion.CASCADE, related_name='gifts', to='disclosures.FinancialDisclosure')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('page_number', models.IntegerField(help_text='The page number the investment is listed on.  This is usedto generate links directly to the PDF page.')),
                ('description', models.TextField(blank=True, help_text='Name of investment (ex. APPL common stock).')),
                ('redacted', models.BooleanField(default=False, help_text='Does the investment row contains redaction(s)?')),
                ('income_during_reporting_period_code', models.CharField(blank=True, choices=[('A', '1 - 1,000'), ('B', '1,001 - 2,500'), ('C', '2,501 - 5,000'), ('D', '5,001 - 15,000'), ('E', '15,001 - 50,000'), ('F', '50,001 - 100,000'), ('G', '100,001 - 1,000,000'), ('H1', '1,000,001 - 5,000,000'), ('H2', '5,000,001 +'), ('-1', 'Failed Extraction')], help_text='Increase in investment value - as a form code', max_length=5)),
                ('income_during_reporting_period_type', models.TextField(blank=True, help_text='Type of investment (ex. Rent, Dividend). Typically standardized but not universally.')),
                ('gross_value_code', models.CharField(blank=True, choices=[('J', '1 - 15,000'), ('K', '15,001 - 50,000'), ('L', '50,001 - 100,000'), ('M', '100,001 - 250,000'), ('N', '250,001 - 500,000'), ('O', '500,001 - 1,000,000'), ('P1', '1,000,001 - 5,000,000'), ('P2', '5,000,001 - 25,000,000'), ('P3', '25,000,001 - 50,000,000'), ('P4', '50,000,001 - '), ('-1', 'Failed Extraction')], help_text='Investment total value code at end of reporting period as code (ex. J (1-15,000)).', max_length=5)),
                ('gross_value_method', models.CharField(blank=True, choices=[('Q', 'Appraisal'), ('R', 'Cost (Real Estate Only)'), ('S', 'Assessment'), ('T', 'Cash Market'), ('U', 'Book Value'), ('V', 'Other'), ('-1', 'Failed Extraction')], help_text='Investment valuation method code (ex. Q = Appraisal)', max_length=5)),
                ('transaction_during_reporting_period', models.TextField(blank=True, help_text='Transaction of investment during reporting period (ex. Buy, Sold)')),
                ('transaction_date_raw', models.CharField(blank=True, help_text='Date of the transaction, if any (D2)', max_length=40)),
                ('transaction_date', models.DateField(blank=True, help_text='Datetime value for if any (D2)', null=True)),
                ('transaction_value_code', models.CharField(blank=True, choices=[('J', '1 - 15,000'), ('K', '15,001 - 50,000'), ('L', '50,001 - 100,000'), ('M', '100,001 - 250,000'), ('N', '250,001 - 500,000'), ('O', '500,001 - 1,000,000'), ('P1', '1,000,001 - 5,000,000'), ('P2', '5,000,001 - 25,000,000'), ('P3', '25,000,001 - 50,000,000'), ('P4', '50,000,001 - '), ('-1', 'Failed Extraction')], help_text='Transaction value amount, as form code (ex. J (1-15,000)).', max_length=5)),
                ('transaction_gain_code', models.CharField(blank=True, choices=[('A', '1 - 1,000'), ('B', '1,001 - 2,500'), ('C', '2,501 - 5,000'), ('D', '5,001 - 15,000'), ('E', '15,001 - 50,000'), ('F', '50,001 - 100,000'), ('G', '100,001 - 1,000,000'), ('H1', '1,000,001 - 5,000,000'), ('H2', '5,000,001 +'), ('-1', 'Failed Extraction')], help_text='Gain from investment transaction if any (ex. A (1-1000)).', max_length=5)),
                ('transaction_partner', models.TextField(blank=True, help_text='Identity of the transaction partner')),
                ('has_inferred_values', models.BooleanField(default=False, help_text='Is the investment name was inferred during extraction.This is common because transactions usually list the firstpurchase of a stock and leave the name value blank for subsequent purchases or sales.')),
                ('financial_disclosure', models.ForeignKey(help_text='The financial disclosure associated with this investment.', on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='disclosures.FinancialDisclosure')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NonInvestmentIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('date_raw', models.TextField(blank=True, help_text='Date of non-investment income (ex. 2011).')),
                ('source_type', models.TextField(blank=True, help_text='Source and type of non-investment income for the judge (ex. Teaching a class at U. Miami).')),
                ('income_amount', models.TextField(blank=True, help_text="Amount earned by judge, often a number, but sometimes with explanatory text (e.g. 'Income at firm: $xyz').")),
                ('redacted', models.BooleanField(default=False, help_text='Does the non-investment income row contain redaction(s)?')),
                ('financial_disclosure', models.ForeignKey(help_text='The financial disclosure associated with this non-investment income.', on_delete=django.db.models.deletion.CASCADE, related_name='non_investment_incomes', to='disclosures.FinancialDisclosure')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('position', models.TextField(blank=True, help_text='Position title (ex. Trustee).')),
                ('organization_name', models.TextField(blank=True, help_text='Name of organization or entity (ex. Trust #1).')),
                ('redacted', models.BooleanField(default=False, help_text='Does the position row contain redaction(s)?')),
                ('financial_disclosure', models.ForeignKey(help_text='The financial disclosure associated with this financial position.', on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='disclosures.FinancialDisclosure')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reimbursement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('source', models.TextField(blank=True, help_text='Source of the reimbursement (ex. FSU Law School).')),
                ('date_raw', models.TextField(blank=True, help_text='Dates as a text string for the date of reimbursements.This is often conference dates (ex. June 2-6, 2011).')),
                ('location', models.TextField(blank=True, help_text='Location of the reimbursement (ex. Harvard Law School, Cambridge, MA).')),
                ('purpose', models.TextField(blank=True, help_text='Purpose of the reimbursement (ex. Baseball announcer).')),
                ('items_paid_or_provided', models.TextField(blank=True, help_text='Items reimbursed (ex. Room, Airfare).')),
                ('redacted', models.BooleanField(default=False, help_text='Does the reimbursement contain redaction(s)?')),
                ('financial_disclosure', models.ForeignKey(help_text='The financial disclosure associated with this reimbursement.', on_delete=django.db.models.deletion.CASCADE, related_name='reimbursements', to='disclosures.FinancialDisclosure')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpouseIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The moment when the item was created.')),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True, help_text='The last moment when the item was modified. A value in year 1750 indicates the value is unknown')),
                ('source_type', models.TextField(blank=True, help_text='Source and type of income of judicial spouse (ex. Salary from Bank job).')),
                ('date_raw', models.TextField(blank=True, help_text='Date of spousal income (ex. 2011).')),
                ('redacted', models.TextField(default=False, help_text='Does the spousal-income row contain redaction(s)?')),
                ('financial_disclosure', models.ForeignKey(help_text='The financial disclosure associated with this spouse income.', on_delete=django.db.models.deletion.CASCADE, related_name='spouse_incomes', to='disclosures.FinancialDisclosure')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='debt',
            name='financial_disclosure',
            field=models.ForeignKey(help_text='The financial disclosure associated with this debt.', on_delete=django.db.models.deletion.CASCADE, related_name='debts', to='disclosures.FinancialDisclosure'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='financial_disclosure',
            field=models.ForeignKey(help_text='The financial disclosure associated with this agreement.', on_delete=django.db.models.deletion.CASCADE, related_name='agreements', to='disclosures.FinancialDisclosure'),
        ),
    ]
