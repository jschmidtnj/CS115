# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
written by Joshua Schmidt 1/17/2018

the program takes an input string of multiple lines, defined by \n, with twitter user
data analytics. the first line of the program designates the range of dates that
this program sorts through.

the program then returns a list of the data provided within the given date range.
'''

#inputted_data = str(input())

inputted_data = """2015-08, 2016-04

2015-08-15, clicks, 635
2016-03-24, app_installs, 683"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
written by Joshua Schmidt 1/17/2018

the program takes an input string of multiple lines, defined by \n, with twitter user
data analytics. the first line of the program designates the range of dates that
this program sorts through.

the program then returns a list of the data provided within the given date range.
'''
data_line_separated = []
for s in inputted_data[2:]:
    data_line_separated.append(s.replace('\n', ''))
start_date, end_date = inputted_data[0].replace('\n', '').split(',')
start_year, start_month = start_date.split('-')
end_year, end_month = end_date.split('-')
start_year, start_month, end_year, end_month = int(start_year), int(start_month), int(end_year), int(end_month)
results = []
for x in data_line_separated:
    #print(x)
    store = False
    date_excluding_day = x[:7]
    year, month = date_excluding_day.split('-')
    int_year, int_month = int(year), int(month)
    if int_year > start_year and int_year < end_year:
        store = True
    elif int_year == start_year and int_month >= start_month:
        store = True
    elif int_year == end_year and int_month <= end_month:
        store = True
    if store == True:
        result_data = str(year) + "-" + str(month) + x[10:]
        results.append(result_data)

for s in results:
    print(s)