def getDestinationFileName(DESTINATION_PATH, LEVEL, LEVEL_BASE, FILTER):
    destinationFileName = DESTINATION_PATH + 'packages_' + LEVEL_BASE
    if FILTER :
        destinationFileName = destinationFileName + '_' + FILTER
    destinationFileName = destinationFileName + '_L' + str(LEVEL) + '_auto.plantuml'
    return destinationFileName

def ifLevel(package, LEVEL):
    return package.count(".") == LEVEL

def isFilter(package, FILTER):
    filters = FILTER.split("|")
    for filter in filters:
        if filter in package:
            return True
    return False

def getLevelPackageName(packageLargeName, LEVEL, LEVEL_BASE):
    package = packageLargeName.split(".")
    packageName = package[0]
    if len(package) > LEVEL:
        for i in range(1, LEVEL+1):
            packageName += "." + package[i]
    if not isFilter(packageName, LEVEL_BASE):
        packageName = getLevelPackageName(packageName, LEVEL-1, "")
    return packageName

def isNeededRelationship(firstPackageLevelName, secondPackageLevelName, FILTER):
    return firstPackageLevelName != secondPackageLevelName and (isFilter(firstPackageLevelName, FILTER) or isFilter(secondPackageLevelName, FILTER))

def setRelationship(relationships, line, LEVEL, LEVEL_BASE, FILTER):
    relationship = line.strip().split(" ")
    firstPackageLevelName = getLevelPackageName(relationship[0], LEVEL, LEVEL_BASE)
    secondPackageLevelName = getLevelPackageName(relationship[2], LEVEL, LEVEL_BASE)
    if ifLevel(firstPackageLevelName, LEVEL) and ifLevel(secondPackageLevelName, LEVEL):
        if isNeededRelationship(firstPackageLevelName, secondPackageLevelName, FILTER):
            relationships.add(firstPackageLevelName + " " + relationship[1] + " " + secondPackageLevelName)

def setBidirectionalRelationship(relationships):
    relationshipsWithBidirectional = set()
    for relationship in relationships:
        relationshipArray = relationship.strip().split(" ")
        rightToLeftRelationship = relationshipArray[2] + " " + relationshipArray[1] + " " + relationshipArray[0]
        if rightToLeftRelationship in relationships:
            bidirectionalRelationshipOtherWay = relationshipArray[2] + " -- " + relationshipArray[0]
            if bidirectionalRelationshipOtherWay not in relationshipsWithBidirectional:
                relationshipsWithBidirectional.add(relationshipArray[0] + " -- " + relationshipArray[2])
        else:
            relationshipsWithBidirectional.add(relationship)

    return relationshipsWithBidirectional
def getPackages(relationships):
    packages = set()
    for relationship in relationships:
        relationshipArray = relationship.strip().split(" ")
        packages.add("package \"" + relationshipArray[0] + "\" as " + relationshipArray[0] + " {}")
        packages.add("package \"" + relationshipArray[2] + "\" as " + relationshipArray[2] + " {}")
    return packages

def getPackageName(line):
    return line.split("\"")[1]

def getLevelUml(sourceFile, LEVEL, LEVEL_BASE, FILTER):
    content = ""
    packages = set()
    relationships = set()
    for line in sourceFile:
        if "@startuml" in line:
            content += '@startuml packages_' + LEVEL_BASE + '_L' + str(LEVEL) + '_auto\n'
        elif "package " in line and ifLevel(getPackageName(line),LEVEL):
            if isFilter(getPackageName(line), LEVEL_BASE):
                packages.add(line.strip() + "}")
        elif "-->" in line:
            setRelationship(relationships, line, LEVEL,LEVEL_BASE, FILTER)
    relationships = setBidirectionalRelationship(relationships)
    if FILTER:
        content += "\n".join(getPackages(relationships)) + "\n"
    else:
        content += "\n".join(packages) + "\n"
    content += "\n".join(relationships)
    content += "\n@enduml"
    return content

#config level 1 all
LEVEL = 1
LEVEL_BASE = "django"
FILTER = ""

#config level 1 filtrado
#LEVEL = 1
#LEVEL_BASE = "django"
#FILTER = "test"

#config level 2 all
#LEVEL = 2
#LEVEL_BASE = "django.views"
#FILTER = ""

#config level 2 filtrado
#LEVEL = 2
#LEVEL_BASE = "django.utils"
#FILTER = "functional"
#FILTER = "format|translation"

#config level 3 all
#LEVEL = 3
#LEVEL_BASE = "django.middleware.clickjacking"
#FILTER = ""

DESTINATION_PATH = '../django/'
sourceFileName = '../django/packages_django.plantuml'

sourceFile = open(sourceFileName)
destinationFile = open(getDestinationFileName(DESTINATION_PATH, LEVEL, LEVEL_BASE, FILTER), 'w')
content = getLevelUml(sourceFile, LEVEL, LEVEL_BASE, FILTER)
destinationFile.write(content)
destinationFile.close()
print('Terminado')
