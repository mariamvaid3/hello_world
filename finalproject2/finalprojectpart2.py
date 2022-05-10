#mariam vaid
#1477614


import csv
from operator import itemgetter
import datetime

#initiating lists to put all the csv data in
gpa=[]
major=[]
grad=[]

with open('/Users/Desktop/StudentsMajorsList.csv') as stulist:
    stuma = csv.reader(stulist)
    for line in stuma:
        major.append(line)

with open('/Users/Desktop/GPAList.csv') as gpalist:
    gp = csv.reader(gpalist)
    for line in gp:
        gpa.append(line)

with open('/Users/Desktop/GraduationDatesList.csv') as gradlist:
    gr = csv.reader(gradlist)
    for line in gr:
        grad.append(line)

new_gpa=(sorted(gpa, key=itemgetter(0)))
new_major=(sorted(major, key=itemgetter(0)))
new_grad=(sorted(grad, key=itemgetter(0)))

for x in range(0,len(new_major)):
    new_major[x].append(gpa[x][1])
for x in range(0, len(new_major)):
        new_major[x].append(grad[x][1])
final_list = new_major
full_roster = (sorted(final_list, key=itemgetter(1)))
print(full_roster)


while True:
    #part v
    q = input("Enter Major or GPA: ")
    if (q == "q"):
        break
    else:
#part i
        major = "" 
        gpa = "" 
        for x in full_roster:
            for i in x[3]:
                if i in q:
                    major = i
            for i in x[5]:
                if i in q:
                    gpa = i
            if major == "" or gpa == "":
                print('no such students')
            else:
                students = ["", "", "", 0]
            # part ii
                for x in full_roster:
                    current_day = datetime.date.today()
                    formatted_date = datetime.date.strftime(current_day, "%m/%d/%Y")
                    if x[6] > formatted_date and x[4] != 'Y' and x[5] >= '0.1':
                        print('Your student(s):', x[0] + " " + x[1] + " " + x[2] + " " + x[3] + " " + x[5])
                    else:
                        print('no such student on the roster')
            # part iii
                for x in full_roster:
                    current_day = datetime.date.today()
                    formatted_date = datetime.date.strftime(current_day, "%m/%d/%Y")
                    if x[6] > formatted_date and x[4] != 'Y' and x[5] >= '0.25':
                        print('You may, also, consider:', x[0] + " " + x[1] + " " + x[2] + " " + x[5])
            #part iv
                for x in full_roster:
                    if x[6] > '5/9/2022' and x[4] != 'Y':
                        print('Other information about student:', x[0] + " " + x[1] + " " + x[2] +"'s" , "graduation date:", x[6])










