#import modules
import os
import csv
import datetime as dt
import re

emp_id = []
name = []
DOB = []
SSN = []
state = []
first_name = []
last_name = []

us_state_abbrev = { 'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
                    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
                    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
                    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
                    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
                    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
                    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
                    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
                   }

csvpath1 = os.path.join("employee_data2.csv")

with open(csvpath1, "r", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        emp_id.append(row[0])
        name = row[1].split()
        first_name.append(name[0])
        last_name.append(name[1])
        date = dt.datetime.strptime(row[2],'%Y-%m-%d').strftime('%d/%m/%Y')
        DOB.append(date)
        SSN.append(re.sub('\d','*',row[3],count=5))
        state.append(us_state_abbrev[row[4]])

path = os.path.join("../PyBoss", "Formatted_"+ csvpath1)

emp_rec = ()
emp_rec = zip(emp_id,  first_name, last_name, DOB, SSN, state )

with open(path, 'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB', 'SSN','State'])
    for emp_id,  first_name, last_name, DOB, SSN, state in emp_rec:
        csvwriter.writerow([emp_id,  first_name, last_name, DOB, SSN, state])