import sys
import os
import matplotlib.pyplot as plt
from matplotlib import dates
from ODM2.Core.services import readCore as CSread
from ODM2.Core.services import CoreServices
from ODM2.SamplingFeatures.services import readSamplingFeatures as SFread
from ODM2.Results.services import readResults as Rread
from ODMconnection import dbconnection


this_file = os.path.realpath(__file__)
directory = os.path.dirname(this_file)
sys.path.insert(0, directory)


# Create a connection to the ODM2 database
# ----------------------------------------


#conn = dbconnection.createConnection('mysql', 'localhost', 'odm2', 'ODM', 'ODM123!!')
conn = dbconnection.createConnection('mysql', 'jws.uwrl.usu.edu', 'odm2', 'ODM', 'ODM123!!')
#conn = dbconnection.createConnection('mssql', '(local)', 'ODM2SS', 'ODM', 'odm')

#conn = dbconnection.createConnection('postgresql', 'arroyo.uwrl.usu.edu:5432', 'ODMSS', 'Stephanie', 'odm')
#conn = dbconnection.createConnection('mysql', '127.0.0.1:3306', 'ODM2', 'Stephanie', 'odm')


# Create a connection for each of the schemas. Currently the schemas each have a different
# connection but it will be changed to all the services sharing a connection
# ----------------------------------------------------------------------------------------
core_read = CSread(conn)
core = CoreServices(conn)
result_read = Rread(conn)
sampfeat_read = SFread(conn)


# Run some basic sample queries.
# ------------------------------
# Get all of the variables from the database and print their names to the console
allVars = core_read.getVariables()
numVars = len(allVars)
print "\n------------ Simple Variables Query ---------------"
print "There are " + str(numVars) + " Variables in the ODM2 database retrieved using getVariables()."
print "The list of variables includes:"
for x in allVars:
    print x.VariableCode + ": " + x.VariableNameCV


# Get all of the people from the database
allPeople = core_read.getPeople()
numPeople = len(allPeople)
print "\n------------ Simple People Query ------------------"
print "There are " + str(numPeople) + " People in the ODM2 database retrieved using getPeople()."
print "The list of People includes: "
for x in allPeople:
    print x.PersonFirstName + " " + x.PersonLastName


# Get all of the SamplingFeatures from the database that are Sites
try:
    siteFeatures = core_read.getSamplingFeaturesByType('Site')
    numSites = len(siteFeatures)
    print "\n--------------- Information about Site SamplingFeatures ------------"
    print "There are " + str(numSites) + " Site SamplingFeatures in the ODM2 database retrieved using getSamplingFeaturesByType()."
    print "The list of Site SamplingFeatures includes: "
    for x in siteFeatures:
        print x.SamplingFeatureCode + ": " + x.SamplingFeatureName
except Exception as e:
    print "Unable to demo getSamplingFeaturesByType", e


# Now get the SamplingFeature object for a SamplingFeature code

try:
    sf = core_read.getSamplingFeatureByCode('USU-LBR-Mendon')
    print "\n-------- Information about an individual SamplingFeature ---------"
    print ("The following are some of the attributes of a SamplingFeature retrieved using getSamplingFeatureByCode(): \n" +
           "SamplingFeatureCode: " + sf.SamplingFeatureCode + "\n" +
           "SamplingFeatureName: " + sf.SamplingFeatureName + "\n" +
           "SamplingFeatureDescription: " + sf.SamplingFeatureDescription + "\n" +
           "SamplingFeatureGeotypeCV: " + sf.SamplingFeatureGeotypeCV + "\n"
           "SamplingFeatureGeometry: " + sf.FeatureGeometry + "\n" +
           "Elevation_m: " + str(sf.Elevation_m))
except Exception as e:
    print "Unable to demo getSamplingFeatureByCode: ", e




# Drill down and get objects linked by foreign keys
print "\n------------ Foreign Key Example --------- \n",
try:
    # Call getResults, but return only the first result
    firstResult = core_read.getResults()[0]
    print "The FeatureAction object for the Result is: ", firstResult.FeatureActionObj
    print "The Action object for the Result is: ", firstResult.FeatureActionObj.ActionObj
    print ("\nThe following are some of the attributes for the Action that created the Result: \n" +
           "ActionTypeCV: " + firstResult.FeatureActionObj.ActionObj.ActionTypeCV + "\n" +
           "ActionDescription: " + firstResult.FeatureActionObj.ActionObj.ActionDescription + "\n" +
           "BeginDateTime: " + str(firstResult.FeatureActionObj.ActionObj.BeginDateTime) + "\n" +
           "EndDateTime: " + str(firstResult.FeatureActionObj.ActionObj.EndDateTime) + "\n" +
           "MethodName: " + firstResult.FeatureActionObj.ActionObj.MethodObj.MethodName + "\n" +
           "MethodDescription: " + firstResult.FeatureActionObj.ActionObj.MethodObj.MethodDescription)
except Exception as e:
    print "Unable to demo Foreign Key Example: ", e


# Now get a particular Result using a ResultID
print "\n------- Example of Retrieving Attributes of a Time Series Result -------"
try:
    tsResult = result_read.getTimeSeriesResultByResultId(19)
    print ("The following are some of the attributes for the TimeSeriesResult retrieved using getTimeSeriesResultByResultID(): \n" +
           "ResultTypeCV: " + tsResult.ResultTypeCV + "\n" +
           # Get the ProcessingLevel from the TimeSeriesResult's ProcessingLevel object
           "ProcessingLevel: " + tsResult.ProcessingLevelObj.Definition + "\n" +
           "SampledMedium: " + tsResult.SampledMediumCV + "\n" +
           # Get the variable information from the TimeSeriesResult's Variable object
           "Variable: " + tsResult.VariableObj.VariableCode + ": " + tsResult.VariableObj.VariableNameCV + "\n"
           "AggregationStatistic: " + tsResult.AggregationStatisticCV + "\n" +
           "Elevation_m: " + str(sf.Elevation_m) + "\n" +
           # Get the site information by drilling down
           "SamplingFeature: " + tsResult.FeatureActionObj.SamplingFeatureObj.SamplingFeatureCode + " - " +
           tsResult.FeatureActionObj.SamplingFeatureObj.SamplingFeatureName)
except Exception as e:
    print "Unable to demo Example of retrieving Attributes of a time Series Result: ", e

# Get the values for a particular TimeSeriesResult
print "\n-------- Example of Retrieving Time Series Result Values ---------"

tsValues = result_read.getTimeSeriesResultValuesByResultId(19) #Return type is a pandas dataframe
# Print a few Time Series Values to the console
#tsValues.set_index('ValueDateTime', inplace=True)
print tsValues.head()
# Plot the time series
fig = plt.figure()
ax = fig.add_subplot(111)
tsValues.plot(x='ValueDateTime',y='DataValue',kind='line',
              title=tsResult.VariableObj.VariableNameCV + " at " + tsResult.FeatureActionObj.SamplingFeatureObj.SamplingFeatureName,
              ax=ax)
ax.set_ylabel(tsResult.VariableObj.VariableNameCV + " (" + tsResult.UnitObj.UnitsAbbreviation +")")

ax.set_xlabel("Date/Time")
ax.xaxis.set_minor_locator(dates.MonthLocator())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
ax.xaxis.set_major_locator(dates.YearLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('\n%Y'))
ax.grid(True)
plt.show()
'''
ax.set_title(tsResult.VariableObj.VariableNameCV + " at " + tsResult.FeatureActionObj.SamplingFeatureObj.SamplingFeatureName)
fig.tight_layout()
fig.savefig('./testfigure.png')
'''



