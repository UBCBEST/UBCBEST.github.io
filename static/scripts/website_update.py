#####################################################################################
#   Author      : Andrew Yan                                                        #
#   Filename    : website_update.py                                                 #
#   Purpose     : Converts current UBC BEST Roster from a .csv file to the          #
#                 appropriate .json files.                                          #
#   Requirements: This script is meant to run with Python 3.6.6 or later            #
#   Versions    :                                                                   #
#                   Vers.# |      Date        |    Name    |    Change Notes        #
#                   1.0     January 20, 2019    Andrew Yan  Initial File            #
#####################################################################################

import os
import csv

name = []
role = []
proj = []
year = []
department = []
biomedicalFlag = []
undergradFlag = []
bio = []
manBio = []
imageName = []
person = [name, role, proj, year, department, biomedicalFlag, undergradFlag, bio, manBio, imageName]

projectID = []
projectIcon = []
projectTab = []
projectName = []
projectAbbr = []
projectDesc = []
project = [projectID, projectIcon, projectTab, projectName, projectAbbr, projectDesc]

currentPath = os.path.abspath(os.path.dirname(__file__))
teamRosterFilePath = os.path.join(currentPath, '../csv/teamRoster.csv')
projectInfoFilePath = os.path.join(currentPath, '../csv/projectsFile.csv')
projectDataFilePath = os.path.join(currentPath, '../data/projectsData.json')

projectData = open(projectDataFilePath, "w")
	

with open(projectInfoFilePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count > 0):
            count = 0
            for projInfo in project:
                project[count].append(line_count - 1)
                project[count][line_count - 1] = row[count]
                count = count + 1
         
        line_count = line_count + 1
        
with open(teamRosterFilePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count > 0):
            count = 0
            for dataIndex in person:
                person[count].append(line_count - 1)
                if (count != 9):
                    person[count][line_count - 1] = row[count]
                count = count + 1
        line_count = line_count + 1
        
i = 0
for index in imageName:
    departmentTemp = department[i]
    if(departmentTemp == "ELEC"):
        department[i] = "Electrical Engineering"
    elif(departmentTemp == "MECH"):
        department[i] = "Mechanical Engineering"
    elif(departmentTemp == "IGEN"):
        department[i] = "Integrated Engineering"
    elif(departmentTemp == "BMEG"):
        department[i] = "Biomedical Engineering"
    elif(departmentTemp == "CHBE"):
        department[i] = "Chemical and Biological Engineering"
    elif(departmentTemp == "ENG PHYS"):
        department[i] = "Engineering Physics"
    elif(departmentTemp == "MTRL"):
        department[i] = "Materials Engineering"
    elif(departmentTemp == "CPEN"):
        department[i] = "Computer Engineering"
    else:
        department[i] = departmentTemp
        
    yearTemp = year[i]
    if (yearTemp == "1"):
        year[i] = "1st"
    elif (yearTemp == "2"):
        year[i] = "2nd"
    elif (yearTemp == "3"):
        year[i] = "3rd"
    else:
        year[i] = yearTemp + "th"
        
    imageTemp = name[i]
    imageTemp = str.lower(imageTemp)
    imageTemp = imageTemp.replace(" ", "-")
    imageName[i] = imageTemp
    i = i + 1

projIndex = 0
projComma = 0
memberComma = 0

projectData.write("{\n")
projectData.write("    \"data\": [\n")
for projInfo in projectID:   
    if (projComma == 1):
        projectData.write(",\n")
        projComma = 0
    projectData.write("        {\n")
    projectData.write("            \"id\": \"%s\",\n" % (projectID[projIndex]))
    projectData.write("            \"icon\": \"%s\",\n" % (projectIcon[projIndex]))
    projectData.write("            \"tab\": \"%s\",\n" % (projectTab[projIndex]))
    projectData.write("            \"name\": \"%s\",\n" % (projectName[projIndex]))
    projectData.write("            \"abbr\": \"%s\",\n" % (projectAbbr[projIndex]))
    projectData.write("            \"desc\": [\n")
    projectData.write("                \"%s\"\n" % (projectDesc[projIndex]))
    projectData.write("            ],\n")
    projectData.write("            \"members\": [\n")
    
    projComma = 1
        
    memberIndex = 0
    for memberCycle in name:
        if((proj[memberIndex] == projectAbbr[projIndex]) & (role[memberIndex] == "Project Lead")):
            if(memberComma == 1):
                projectData.write(",\n")
                memberComma = 0
            projectData.write("                {\n")
            projectData.write("                    \"name\": \"%s\",\n" % (name[memberIndex]))
            projectData.write("                    \"position\": \"%s\",\n" % (role[memberIndex]))
            relativeImagePath1 = "../img/projects/" + projectID[projIndex] + "/" + imageName[memberIndex] + ".jpg"
            relativeImagePath2 = "../img/projects/" + projectID[projIndex] + "/" + imageName[memberIndex] + ".png"
            imagePath1 = os.path.join(currentPath, relativeImagePath1)
            imagePath2 = os.path.join(currentPath, relativeImagePath2)
            if os.path.exists(imagePath1):
                projectData.write("                    \"img\": \"static/img/projects/%s/%s.jpg\",\n" % (projectID[projIndex], imageName[memberIndex]))
            elif os.path.exists(imagePath2):
                projectData.write("                    \"img\": \"static/img/projects/%s/%s.png\",\n" % (projectID[projIndex], imageName[memberIndex]))
            else:
                projectData.write("                    \"img\": \"\",\n")
            projectData.write("                    \"year\": \"%s\",\n" % (year[memberIndex]))
            projectData.write("                    \"department\": \"%s\",\n" % (department[memberIndex]))
            if (biomedicalFlag[memberIndex] == '1'):
                projectData.write("                    \"biomed\": true,\n")
            else:
                projectData.write("                    \"biomed\": false,\n")
            projectData.write("                    \"desc\": \"%s\"\n" % (bio[memberIndex]))   
            projectData.write("                }")
            memberComma = 1
        memberIndex = memberIndex + 1
        
    memberIndex = 0
    for memberCycle in name:
        if((proj[memberIndex] == projectAbbr[projIndex]) & (role[memberIndex] != "Project Lead")):
            if(memberComma == 1):
                projectData.write(",\n")
                memberComma = 0
            projectData.write("                {\n")
            projectData.write("                    \"name\": \"%s\",\n" % (name[memberIndex]))
            projectData.write("                    \"position\": \"%s\",\n" % (role[memberIndex]))
            relativeImagePath1 = "../img/projects/" + projectID[projIndex] + "/" + imageName[memberIndex] + ".jpg"
            relativeImagePath2 = "../img/projects/" + projectID[projIndex] + "/" + imageName[memberIndex] + ".png"
            
            imagePath1 = os.path.join(currentPath, relativeImagePath1)
            imagePath2 = os.path.join(currentPath, relativeImagePath2)
            if os.path.exists(imagePath1):
                projectData.write("                    \"img\": \"static/img/projects/%s/%s.jpg\",\n" % (projectID[projIndex], imageName[memberIndex]))
            elif os.path.exists(imagePath2):
                projectData.write("                    \"img\": \"static/img/projects/%s/%s.png\",\n" % (projectID[projIndex], imageName[memberIndex]))
            else:
                projectData.write("                    \"img\": \"\",\n")
            projectData.write("                    \"year\": \"%s\",\n" % (year[memberIndex]))
            projectData.write("                    \"department\": \"%s\",\n" % (department[memberIndex]))
            if (biomedicalFlag[memberIndex] == '1'):
                projectData.write("                    \"biomed\": true,\n")
            else:
                projectData.write("                    \"biomed\": false,\n")
            projectData.write("                    \"desc\": \"%s\"\n" % (bio[memberIndex]))   
            projectData.write("                }")
            memberComma = 1
        memberIndex = memberIndex + 1
    if(memberComma == 1):
        projectData.write("\n")
        memberComma = 0
    projectData.write("            ]\n")
    projectData.write("        }")

    projIndex  = projIndex + 1

projectData.write("\n")
projectData.write("    ]\n") 
projectData.write("}\n")
projectData.close()
    
