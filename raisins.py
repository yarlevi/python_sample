"""
Generate VCARD per employee in Excel file
"""
import csv

vcard_template = '''
BEGIN:VCARD
VERSION:2.1
N:Bunny;Bugs
FN:Bugs Bunny
ORG:Looney Tunes
TITLE:SVP Carrot Eating
TEL;WORK;VOICE:555-555-5555
ADR;WORK:;;1 Carrot Ave.;Los Angels;CA;90583;United States of America
EMAIL;PREF;INTERNET:bugs@looney.com
REV:20140609T195243Z
END:VCARD
'''

#Get
fp=open('raisin_team.csv')

# Parse
for fields in csv.reader(fp):
           print fields
# Analyze
# Output
