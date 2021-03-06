import csv
import json
import re

# Hold parsed data
data = []

# Constants
MAX_GROUP_SIZE = 6
DEGREE_INDEX = 3
SPECIALIZATION_INDEX = 4
MINOR1_INDEX = 5
MINOR2_INDEX = 6
COOP_INDEX = 7
DISTINCTION_INDEX = 8
MEDAL_INDEX = 10
FULLNAME_INDEX = 11

def getFullname(row):
    return re.sub("\s\s+" , " ", row[FULLNAME_INDEX].rstrip())

def getDistinction(row):
    if "Honours" in row[DISTINCTION_INDEX]:
        return "With Honours"
    elif "With High Distinction" in row[DISTINCTION_INDEX]:
        return "With High Distinction"
    elif "With Distinction" in row[DISTINCTION_INDEX]:
        return "With Distinction"

def getDegree(row):
    if "Bachelor of Computer Science Major" in row[DEGREE_INDEX].rstrip():
        return "Bachelor of Computer Science Major"
    elif "Bachelor of Computer Science" in row[DEGREE_INDEX].rstrip():
        return "Bachelor of Computer Science Honours"
    elif "Master of Arts Human-Computer Interaction" in row[DEGREE_INDEX].rstrip():
        return "Master of Arts Human-Computer Interaction"
    elif "Master of Computer Science" in row[DEGREE_INDEX].rstrip():
        return "Master of Computer Science"
    elif "Doctor of Philosophy" in row[DEGREE_INDEX].rstrip():
        return "Doctor of Philosophy Computer Science"
    elif "Master of Applied Science" in row[DEGREE_INDEX].rstrip():
        return "Master of Applied Science"
    elif "Master of Arts" in row[DEGREE_INDEX].rstrip():
        return "Master of Arts"

def getSpecialization(row):
    if "Specialization in Data Science" in row[SPECIALIZATION_INDEX]:
        return "Specialization in Data Science"
    if "Human-Computer Interaction" in row[SPECIALIZATION_INDEX]:
        return "Human-Computer Interaction"

def getMinors(row):
    minors = []

    if len(row[MINOR1_INDEX]) > 1:
        minors.append(row[MINOR1_INDEX].rstrip())

    if len(row[MINOR2_INDEX]) > 1:
        minors.append(row[MINOR2_INDEX].rstrip())

    return minors

def getCoop(row):
    if len(row[COOP_INDEX]) > 1:
        return True
    elif "Master of Computer Science" in row[DEGREE_INDEX]:
        if "Co-operative Education" in row[SPECIALIZATION_INDEX]:
            return True

    return False

def getMedal(row):
    if len(row[MEDAL_INDEX]) > 2:
        return row[MEDAL_INDEX].rstrip()

# Parse data
with open('graduates4.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    group = []

    for row in csv_reader:
        print(getDegree(row))
        if "Name" not in row[0]:
            student = {
                "fullname": getFullname(row),
                "degree": getDegree(row),
                "distinction": getDistinction(row),
                "specialization": getSpecialization(row),
                "minors": getMinors(row),
                "coop": getCoop(row),
                "medal": getMedal(row)
            }

            group.append(student)

            if len(group) >= MAX_GROUP_SIZE:
                data.append(group)
                group = []

    data.append(group)

# Serializing json
json_object = json.dumps(data, indent = 4)

# Writing to sample.json
with open("data.json", "w") as outfile:
    outfile.write(json_object)
