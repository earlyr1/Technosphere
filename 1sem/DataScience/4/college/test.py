import pandas as pd 

a1 = pd.read_csv("salaries-by-college-type.csv")
a2 = pd.read_csv("salaries-by-region.csv")

print a1[a1['School Type'] == 'State'].count()
#print a2

a3 = a2.merge(a1, left_on = 'School Name')
#a3['Starting Median Salary']
