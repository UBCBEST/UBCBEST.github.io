#####################################################################################
#   Author      : Andrew Yan                                                        #
#   Filename    : website_update.py                                                 #
#   Purpose     : Converts current UBC BEST Roster from a .csv file to the          #
#                 appropriate .json files.                                          #
#   Requirements: This script is meant to run with Python 3.6.6 or later            #
#   Versions    :                                                                   #
#                   Vers.# |      Date        |    Name    |    Change Notes        #
#                   1.0     January 20, 2019    Andrew Yan  Initial File            #
#                   2.0     September 10, 2019  Andrew Yan  Updated to auto populate#
#                                                           teamsData.json          #
#####################################################################################

import os
import csv

name = []
role = []
proj = []
role2 = []
proj2 = []
year = []
department = []
biomedicalFlag = []
undergradFlag = []
bio = []
manBio = []
imageName = []
person = [name, role, proj, role2, proj2, year, department, biomedicalFlag, undergradFlag, bio, manBio, imageName]

projectID = []
projectIcon = []
projectTab = []
projectName = []
projectAbbr = []
projectDesc = []
teamID = []
teamIcon = []
teamTab = []
teamName = []
project = [projectID, projectIcon, projectTab, projectName, projectAbbr, projectDesc]
team = [teamID, teamIcon, teamTab, teamName]

currentPath = os.path.abspath(os.path.dirname(__file__))
teamRosterFilePath = os.path.join(currentPath, '../csv/teamRoster.csv')
projectInfoFilePath = os.path.join(currentPath, '../csv/projectsFile.csv')
teamInfoFilePath = os.path.join(currentPath, '../csv/teamsFile.csv')
alumniListFilePath = os.path.join(currentPath, '../csv/alumniList.csv')
sponsorListFilePath = os.path.join(currentPath, '../csv/sponsorList.csv')
advisorListFilePath = os.path.join(currentPath, '../csv/advisorList.csv')

projectDataFilePath = os.path.join(currentPath, '../data/projectsData.json')
teamDataFilePath = os.path.join(currentPath, '../data/teamsData.json')

projectData = open(projectDataFilePath, "w")
teamsData = open(teamDataFilePath, "w")

with open(teamInfoFilePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count > 0):
            count = 0
            for teamInfo in team:
                team[count].append(line_count - 1)
                team[count][line_count - 1] = row[count]
                count = count + 1
         
        line_count = line_count + 1    
    
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

#Adds current members to the list, creates a copy of project leads so that they can also exist under the management tab        
with open(teamRosterFilePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count > 0):
            count = 0
            for dataIndex in person:
                person[count].append(line_count - 1)
                if (count != 11):
                    person[count][line_count - 1] = row[count]
                count = count + 1
            if (role[line_count-1] == "Project Lead"):
                count = 0
                for dataIndex in person:
                    person[count].append(line_count)
                    person[count][line_count] = person[count][line_count-1]
                    count = count + 1
                role[line_count] = proj[line_count] + " Project Lead"
                proj[line_count] = "MAN"
                role2[line_count] = ""
                proj2[line_count] = ""
                line_count = line_count + 1
            if (role2[line_count-1] == "Project Lead"):
                count = 0
                for dataIndex in person:
                    person[count].append(line_count)
                    person[count][line_count] = person[count][line_count-1]
                    count = count + 1
                role[line_count] = proj2[line_count] + " Project Lead"
                proj[line_count] = "MAN"
                role2[line_count] = ""
                proj2[line_count] = ""
                
                line_count = line_count + 1    
                
        line_count = line_count + 1

#Adds alumni to the list        
with open(alumniListFilePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        count = 0
        for dataIndex in person:
            person[count].append(line_count - 1)
            person[count][line_count - 1] = ""
            count = count + 1
        name[line_count - 1] = row[0]
        proj[line_count - 1] = "ALUM"
        role[line_count - 1] = "Alumni"
        line_count = line_count + 1
        
#Adds sponsor to the list        
with open(sponsorListFilePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        count = 0
        for dataIndex in person:
            person[count].append(line_count - 1)
            person[count][line_count - 1] = ""
            count = count + 1
        name[line_count - 1] = row[0]
        proj[line_count - 1] = "SPON"
        role[line_count - 1] = "Sponsor"
        line_count = line_count + 1

#Adds advisor to the list        
with open(advisorListFilePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        count = 0
        for dataIndex in person:
            person[count].append(line_count - 1)
            person[count][line_count - 1] = ""
            count = count + 1
        name[line_count - 1] = row[0]
        proj[line_count - 1] = "ADV"
        role[line_count - 1] = "Advisor"
        line_count = line_count + 1
        
#Puts data into correct format
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

#writes out the projectsData.json file
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
        if(((proj[memberIndex] == projectAbbr[projIndex]) & (role[memberIndex] == "Project Lead")) | ((role2[memberIndex] == "Project Lead") & (proj2[memberIndex] == projectAbbr[projIndex]))):
            if(memberComma == 1):
                projectData.write(",\n")
                memberComma = 0
            projectData.write("                {\n")
            projectData.write("                    \"name\": \"%s\",\n" % (name[memberIndex]))
            if (role[memberIndex] == "Project Lead"):
                projectData.write("                    \"position\": \"%s\",\n" % (role[memberIndex]))
            else:
                projectData.write("                    \"position\": \"%s\",\n" % (role2[memberIndex]))
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
        if(((proj[memberIndex] == projectAbbr[projIndex]) & (role[memberIndex] != "Project Lead")) | ((role2[memberIndex] != "Project Lead") & (proj2[memberIndex] == projectAbbr[projIndex]))):
            if(memberComma == 1):
                projectData.write(",\n")
                memberComma = 0
            projectData.write("                {\n")
            projectData.write("                    \"name\": \"%s\",\n" % (name[memberIndex]))
            if (role[memberIndex] != "Project Lead"):
                projectData.write("                    \"position\": \"%s\",\n" % (role[memberIndex]))
            else:
                projectData.write("                    \"position\": \"%s\",\n" % (role2[memberIndex]))
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

teamComma = 0
teamIndex = 0
memberComma = 0

#writes out the teamsData.json file
teamsData.write("{\n")
teamsData.write("    \"data\": [\n")
for teamInfo in teamID:   
    if (teamComma == 1):
        teamsData.write(",\n")
        teamComma = 0
    teamsData.write("        {\n")
    teamsData.write("            \"id\": \"%s\",\n" % (teamID[teamIndex]))
    teamsData.write("            \"icon\": \"%s\",\n" % (teamIcon[teamIndex]))
    teamsData.write("            \"tab\": \"%s\",\n" % (teamTab[teamIndex]))
    teamsData.write("            \"name\": \"%s\",\n" % (teamName[teamIndex]))
    teamsData.write("            \"members\": [\n")
    
    memberIndex = 0
    memberComma = 0
    for memberCycle in name:
        if ((proj[memberIndex] == str.upper(teamID[teamIndex])) | (proj2[memberIndex] == str.upper(teamID[teamIndex]))):
            if(memberComma == 1):
                teamsData.write(",\n")
                memberComma = 0
            teamsData.write("                {\n")
            teamsData.write("                    \"name\": \"%s\",\n" % (name[memberIndex]))
            if (proj[memberIndex] == str.upper(teamID[teamIndex])):
                teamsData.write("                    \"title\": \"%s\",\n" % (role[memberIndex]))
            else:
                teamsData.write("                    \"title\": \"%s\",\n" % (role2[memberIndex]))
            relativeImagePath1 = "../img/teams/" + teamID[teamIndex] + "/" + imageName[memberIndex] + ".jpg"
            relativeImagePath2 = "../img/teams/" + teamID[teamIndex] + "/" + imageName[memberIndex] + ".png"
            imagePath1 = os.path.join(currentPath, relativeImagePath1)
            imagePath2 = os.path.join(currentPath, relativeImagePath2)
            if os.path.exists(imagePath1):
                teamsData.write("                    \"img\": \"static/img/teams/%s/%s.jpg\",\n" % (teamID[teamIndex], imageName[memberIndex]))
            elif os.path.exists(imagePath2):
                teamsData.write("                    \"img\": \"static/img/teams/%s/%s.png\",\n" % (teamID[teamIndex], imageName[memberIndex]))
            else:
                teamsData.write("                    \"img\": \"\",\n")
            teamsData.write("                    \"link\": \"\",\n")
            teamsData.write("                    \"desc\": [\n")
            teamsData.write("                       \"%s\"\n" % (bio[memberIndex]))   
            teamsData.write("                    ]\n")   
            teamsData.write("                }")
            memberComma = 1
        memberIndex = memberIndex + 1
        
    teamsData.write("\n")
    teamsData.write("            ]\n")
    teamsData.write("        }")

    teamComma = 1
    teamIndex  = teamIndex + 1
teamsData.write("\n")
teamsData.write("    ]\n") 
teamsData.write("}\n")

teamsData.close()
    
