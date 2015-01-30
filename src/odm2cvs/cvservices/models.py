from __future__ import unicode_literals

from django.db import models


class ActionType(models.Model):
    term = models.TextField(primary_key=True)
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField()
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)
    producesresult = models.TextField(db_column='producesResult')

    class Meta:
        managed = False
        db_table = 'ActionTypeCV'


class ActionTypeRequest(models.Model):
    requestid = models.TextField(db_column='requestId', primary_key=True)
    status = models.TextField()
    term = models.ForeignKey(ActionType, db_column='term')
    datesubmitted = models.DateField(db_column='dateSubmitted')
    datestatuschanged = models.DateField(db_column='dateStatusChanged')
    requestnotes = models.TextField(db_column='requestNotes')
    submittername = models.TextField(db_column='submitterName')
    submitteremail = models.TextField(db_column='submitterEmail', blank=True)
    requestreason = models.TextField(db_column='requestReason')
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField()
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)
    producesresult = models.TextField(db_column='producesResult')

    class Meta:
        managed = False
        db_table = 'ActionTypeCVRequests'


class MethodType(models.Model):
    term = models.TextField(primary_key=True)
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField()
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'MethodTypeCV'


class MethodTypeRequest(models.Model):
    requestid = models.TextField(db_column='requestId', primary_key=True)
    status = models.TextField()
    term = models.ForeignKey(MethodType, db_column='term')
    datesubmitted = models.DateField(db_column='dateSubmitted')
    datestatuschanged = models.DateField(db_column='dateStatusChanged')
    requestnotes = models.TextField(db_column='requestNotes')
    submittername = models.TextField(db_column='submitterName')
    submitteremail = models.TextField(db_column='submitterEmail', blank=True)
    requestreason = models.TextField(db_column='requestReason')
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField()
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'MethodTypeCVRequests'


class OrganizationType(models.Model):
    term = models.TextField(primary_key=True)
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField(blank=True)
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'OrganizationTypeCV'


class OrganizationTypeRequest(models.Model):
    requestid = models.TextField(db_column='requestId', primary_key=True)
    status = models.TextField()
    term = models.ForeignKey(OrganizationType, db_column='term')
    datesubmitted = models.DateField(db_column='dateSubmitted')
    datestatuschanged = models.DateField(db_column='dateStatusChanged')
    requestnotes = models.TextField(db_column='requestNotes')
    submittername = models.TextField(db_column='submitterName')
    submitteremail = models.TextField(db_column='submitterEmail', blank=True)
    requestreason = models.TextField(db_column='requestReason')
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField(blank=True)
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'OrganizationTypeCVRequests'


class SamplingFeatureGeotype(models.Model):
    term = models.TextField(primary_key=True)
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField()
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'SamplingFeatureGeotypeCV'


class SamplingFeatureGeotypeRequest(models.Model):
    requestid = models.TextField(db_column='requestId', primary_key=True)
    status = models.TextField()
    term = models.ForeignKey(SamplingFeatureGeotype, db_column='term')
    datesubmitted = models.DateField(db_column='dateSubmitted')
    datestatuschanged = models.DateField(db_column='dateStatusChanged')
    requestnotes = models.TextField(db_column='requestNotes')
    submittername = models.TextField(db_column='submitterName')
    submitteremail = models.TextField(db_column='submitterEmail', blank=True)
    requestreason = models.TextField(db_column='requestReason')
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField()
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'SamplingFeatureGeotypeCVRequests'


class SamplingFeatureType(models.Model):
    term = models.TextField(primary_key=True)
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField()
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'SamplingFeatureTypeCV'


class SamplingFeatureTypeRequest(models.Model):
    requestid = models.TextField(db_column='requestId', primary_key=True)
    status = models.TextField()
    term = models.ForeignKey(SamplingFeatureType, db_column='term')
    datesubmitted = models.DateField(db_column='dateSubmitted')
    datestatuschanged = models.DateField(db_column='dateStatusChanged')
    requestnotes = models.TextField(db_column='requestNotes')
    submittername = models.TextField(db_column='submitterName')
    submitteremail = models.TextField(db_column='submitterEmail', blank=True)
    requestreason = models.TextField(db_column='requestReason')
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField()
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'SamplingFeatureTypeCVRequests'


class SiteType(models.Model):
    term = models.TextField(primary_key=True)
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField()
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'SiteTypeCV'


class SiteTypeRequest(models.Model):
    requestid = models.TextField(db_column='requestId', primary_key=True)
    status = models.TextField()
    term = models.ForeignKey(SiteType, db_column='term')
    datesubmitted = models.DateField(db_column='dateSubmitted')
    datestatuschanged = models.DateField(db_column='dateStatusChanged')
    requestnotes = models.TextField(db_column='requestNotes')
    submittername = models.TextField(db_column='submitterName')
    submitteremail = models.TextField(db_column='submitterEmail', blank=True)
    requestreason = models.TextField(db_column='requestReason')
    name = models.TextField()
    definition = models.TextField()
    category = models.TextField()
    provenance = models.TextField(blank=True)
    provenanceuri = models.TextField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'SiteTypeCVRequests'