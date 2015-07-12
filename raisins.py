"""
Generate VCARD per employee in Excel file
"""
import csv

#Get
fp=open('raisin_team.csv')

# Parse
for fields in csv.reader(fp):
           print fields
# Analyze
# Output
