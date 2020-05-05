# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Epicov(models.Model):
    index = models.TextField(blank=True, null=True)
    number_0 = models.TextField(db_column='0', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    age = models.TextField(blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    country_exposure = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    date_submitted = models.TextField(blank=True, null=True)
    division = models.TextField(blank=True, null=True)
    division_exposure = models.TextField(blank=True, null=True)
    genbank_accession = models.TextField(blank=True, null=True)
    gisaid_epi_isl = models.TextField(primary_key=True)
    host = models.TextField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    originating_lab = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    region_exposure = models.TextField(blank=True, null=True)
    segment = models.TextField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    strain = models.TextField(blank=True, null=True)
    submitting_lab = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    virus = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'epicov'

