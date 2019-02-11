'''
Output: _count.xlsx      _result.xlsx  _result.csv
Extracts fraction of xlsx files in which a given email address appears.
The email address column is specified below
It is intentionally mandated to provide the path as first argument. This simplifies housekeeping.
'''
import glob
import pandas as pd
import sys
from collections import defaultdict
import re

# Set the email column here
email_column = 'Email Address'
# set threshold here
threshold = 0.5

if(len(sys.argv)==2):
    path = "" + sys.argv[1]
else:
    print("Please enter path of the folder as first command line argument.")
    exit(0)

location = path + "*.xlsx"
print("Fetching files matching: "+location)

files = glob.glob(location)
print("fetched: " + str(len(files)) + " files")


email_count = defaultdict(int)
for file in files:
    emails = (pd.read_excel(file)[email_column]).unique()
    for email in emails:
        unityid = (re.search(r'([^\.]+).edu*',email)).group(1)
        email_count[unityid] += 1

result = pd.DataFrame.from_dict(email_count,orient='index')
writer = pd.ExcelWriter(path+'_count.xlsx')
result.to_excel(writer)
writer.save()

for email in email_count:
    if(email_count[email]/(len(files)) >= threshold):
        email_count[email]=1
    else:
        email_count[email]=0

writer = pd.ExcelWriter(path+'_result.xlsx')
result = pd.DataFrame.from_dict(email_count,orient='index')
result.to_excel(writer)
writer.save()
result.to_csv(path+"_result.csv")
