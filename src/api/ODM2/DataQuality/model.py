# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
#from ODM2 import modelBase as Base
from ODM2.Core.model import Unit, Variable, Result, Organization, Samplingfeature, Base
from ODM2.Provenance.model import Citation



class Dataquality(Base):
    __tablename__ = 'DataQuality'
    __table_args__ = {u'schema': 'ODM2'}

    DataQualityID = Column(Integer, primary_key=True)
    DataQualityTypeCV = Column(String(255, u'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DataQualityCode = Column(String(255, u'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    DataQualityValue = Column(Float(53))
    DataQualityValueUnitsID = Column(ForeignKey('ODM2.Units.UnitsID'))
    DataQualityDescription = Column(String(500, u'SQL_Latin1_General_CP1_CI_AS'))
    DataQualityLink = Column(String(255, u'SQL_Latin1_General_CP1_CI_AS'))


    UnitObj = relationship(Unit)



class Referencematerial(Base):
    __tablename__ = 'ReferenceMaterials'
    __table_args__ = {u'schema': 'ODM2'}

    ReferenceMaterialID = Column(Integer, primary_key=True)
    ReferenceMaterialMediumCV = Column(String(255, u'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ReferenceMaterialOrganizationID = Column(ForeignKey('ODM2.Organizations.OrganizationID'), nullable=False)
    ReferenceMaterialCode = Column(String(50, u'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    ReferenceMaterialLotCode = Column(String(255, u'SQL_Latin1_General_CP1_CI_AS'))
    ReferenceMaterialPurchaseDate = Column(DateTime)
    ReferenceMaterialExpirationDate = Column(DateTime)
    ReferenceMaterialCertificateLink = Column(String(255, u'SQL_Latin1_General_CP1_CI_AS'))
    SamplingFeatureID = Column(ForeignKey('ODM2.SamplingFeatures.SamplingFeatureID'))

    OrganizationObj = relationship(Organization)
    SamplingFeature = relationship(Samplingfeature)



Resultnormalizationvalue = Table(
    u'ResultNormalizationValues', Base.metadata,
    Column(u'ResultID', ForeignKey('ODM2.Results.ResultID'), primary_key=True),
    Column(u'NormalizedByReferenceMaterialValueID', ForeignKey('ODM2.ReferenceMaterialValues.ReferenceMaterialValueID'), nullable=False),
    schema='ODM2'
)


class Referencematerialvalue(Base):
    __tablename__ = u'ReferenceMaterialValues'
    __table_args__ = {u'schema': 'ODM2'}

    ReferenceMaterialValueID = Column(Integer, primary_key=True)
    ReferenceMaterialID = Column(ForeignKey('ODM2.ReferenceMaterials.ReferenceMaterialID'), nullable=False)
    ReferenceMaterialValue = Column(Float(53), nullable=False)
    ReferenceMaterialAccuracy = Column(Float(53))
    VariableID = Column(ForeignKey('ODM2.Variables.VariableID'), nullable=False)
    UnitsID = Column(ForeignKey('ODM2.Units.UnitsID'), nullable=False)
    CitationID = Column(ForeignKey('ODM2.Citations.CitationID'), nullable=False)

    CitationObj = relationship(Citation)
    ReferenceMaterialObj = relationship(Referencematerial)
    UnitObj = relationship(Unit)
    VariableObj = relationship(Variable)
    ResultsObj = relationship(Result, secondary=Resultnormalizationvalue)


class Resultsdataquality(Base):
    __tablename__ = 'ResultsDataQuality'
    __table_args__ = {u'schema': 'ODM2'}

    BridgeID = Column(Integer, primary_key=True)
    ResultID = Column(ForeignKey('ODM2.Results.ResultID'), nullable=False)
    DataQualityID = Column(ForeignKey('ODM2.DataQuality.DataQualityID'), nullable=False)

    DataQualityObj = relationship(Dataquality)
    ResultObj = relationship(Result)


