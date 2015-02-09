from __future__ import unicode_literals
from django.utils import timezone
from uuid import uuid4

from django.db import models


class ControlVocabulary(models.Model):
    term = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    definition = models.TextField()
    category = models.CharField(max_length=255)
    provenance = models.TextField(blank=True)
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        abstract = True


class ControlVocabularyRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    )
    request_id = models.CharField(max_length=255, db_column='requestId', primary_key=True, default=uuid4)
    status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    date_submitted = models.DateField(db_column='dateSubmitted', default=timezone.now())
    date_status_changed = models.DateField(db_column='dateStatusChanged', default=timezone.now())
    request_notes = models.TextField(db_column='requestNotes')
    submitter_name = models.CharField(max_length=255, db_column='submitterName')
    submitter_email = models.CharField(max_length=255, db_column='submitterEmail', blank=True)
    request_reason = models.CharField(max_length=255, db_column='requestReason')

    class Meta:
        abstract = True


class AbstractActionType(models.Model):
    PRODUCES_RESULT_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    produces_result = models.CharField(db_column='producesResult', max_length=5, choices=PRODUCES_RESULT_CHOICES)

    class Meta:
        abstract = True


class ActionType(ControlVocabulary, AbstractActionType):
    class Meta:
        managed = False
        db_table = 'ActionTypeCV'
        verbose_name = 'Action Type Control Vocabulary'


class ActionTypeRequest(ControlVocabularyRequest, ControlVocabulary, AbstractActionType):
    class Meta:
        managed = False
        db_table = 'ActionTypeCVRequests'
        verbose_name = 'Action Type Control Vocabulary Request'


class MethodType(ControlVocabulary):
    class Meta:
        #managed = False
        db_table = 'MethodTypeCV'
        verbose_name = 'Method Type Control Vocabulary'


class MethodTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'MethodTypeCVRequests'
        verbose_name = 'Method Type Control Vocabulary Request'


class OrganizationType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'OrganizationTypeCV'
        verbose_name = 'Organization Type Control Vocabulary'


class OrganizationTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'OrganizationTypeCVRequests'
        verbose_name = 'Organization Type Control Vocabulary Request'


class SamplingFeatureGeotype(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureGeotypeCV'
        verbose_name = 'Sampling Feature Geo-type Control Vocabulary'


class SamplingFeatureGeotypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureGeotypeCVRequests'
        verbose_name = 'Sampling Feature Geo-type Control Vocabulary Request'


class SamplingFeatureType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureTypeCV'
        verbose_name = 'Sampling Feature Type Control Vocabulary'


class SamplingFeatureTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SamplingFeatureTypeCVRequests'
        verbose_name = 'Sampling Feature Type Control Vocabulary Request'


class SiteType(ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SiteTypeCV'
        verbose_name = 'Site Type Control Vocabulary'


class SiteTypeRequest(ControlVocabularyRequest, ControlVocabulary):
    class Meta:
        managed = False
        db_table = 'SiteTypeCVRequests'
        verbose_name = 'Site Type Control Vocabulary Request'