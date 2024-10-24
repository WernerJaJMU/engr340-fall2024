import sys
import pandas
import numpy
import scipy

def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    # Here I create two lists one to store the rockingham dates and the other to store harrisonburg city dates
    Rockingham_date = []
    Harrisonburg_date = []

    #Here I iterate through the data and find when the county is what im looking for

    for (date, county, state, cases, deaths) in data: #This wouldn't work when i had the fips in there idky
        if county == "Rockingham" and state == "Virginia": # I needed to add an and statement cause there are more than one rockingham
            Rockingham_date.append(date) #Store the date in my list

        if county == "Harrisonburg city": #find harrisonburg
            Harrisonburg_date.append(date)#Store the date in my list

    first_Rockingham = Rockingham_date[0] #take the first value
    first_Harrisonburg = Harrisonburg_date[0] #take the first value

    print(f"The first positive COVID case in Rockingham County was on {first_Rockingham}") #print the value
    print(f"The first positive COVID case in Harrisonburg was on {first_Harrisonburg}") #print the value
    # your code here
    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    #Make a whole bunch of lists
    Rockingham_cases = []
    Harrisonburg_cases = []
    Rockingham_day = []
    Harrisonburg_day = []
    R_dates = []
    H_dates = []

    for (date, county, state, cases, deaths) in data: #same loop as above except im storing dates and case amounts

        if county == "Rockingham" and state == "Virginia":
            Rockingham_cases.append(cases)
            R_dates.append(date)
        if county == "Harrisonburg city":
            Harrisonburg_cases.append(cases)
            H_dates.append(date)

    for i in range(1,len(Rockingham_cases)): #for all the terms in my cases lists iterate from the 1st term to the last
        dayR = (Rockingham_cases[i] - Rockingham_cases[i-1]) #subtract the proceeding term from the next term
        Rockingham_day.append(dayR) #append it to a new list

    for i in range(1,len(Harrisonburg_cases)):
        dayH = (Harrisonburg_cases[i] - Harrisonburg_cases[i-1])
        Harrisonburg_day.append(dayH)

    H_day_max = numpy.max(Harrisonburg_day) #find the max number of cases for one day
    R_day_max = numpy.max(Rockingham_day)

    max_R_index = Rockingham_day.index(R_day_max) #find the index of this list
    max_H_index = Harrisonburg_day.index(H_day_max)

    print(f"The greatest number of new cases in Rockingham County was on {R_dates[max_R_index]}") #use the index of this list for the dates list to find what day the max happened on
    print(f"The greatest number of new cases in Harrisonburg was on {H_dates[max_H_index]}")

    # your code here
    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    Rockingham_cases = []
    Harrisonburg_cases = []
    Rockingham_day = []
    Harrisonburg_day = []
    R_dates = []
    H_dates = []
    seven_day_R = []
    seven_day_H = []

    for (date, county, state, cases, deaths) in data:
        if county == "Rockingham" and state == "Virginia":
            Rockingham_cases.append(cases)
            R_dates.append(date)
        if county == "Harrisonburg city":
            Harrisonburg_cases.append(cases)
            H_dates.append(date)

    for i in range(1,len(Rockingham_cases)): #for all the terms in my cases lists iterate from the 1st term to the last
            dayR = (Rockingham_cases[i] - Rockingham_cases[i-1]) #subtract the proceeding term from the next term
            Rockingham_day.append(dayR) #append it to a new list

    for i in range(1,len(Harrisonburg_cases)):
            dayH = (Harrisonburg_cases[i] - Harrisonburg_cases[i-1])
            Harrisonburg_day.append(dayH)

    for i in range(6,len(Rockingham_day)): #find the sum of new cases for every seven day period and store it
            seven_day_sumR = (Rockingham_day[i-6]+Rockingham_day[i-5]+Rockingham_day[i-4]+Rockingham_day[i-3]+Rockingham_day[i-2]+Rockingham_day[i-1]+Rockingham_day[i])
            seven_day_R.append(seven_day_sumR)

    for i in range(6,len(Harrisonburg_day)):
            seven_day_sumH = (Harrisonburg_day[i-6]+Harrisonburg_day[i-5]+Harrisonburg_day[i-4]+Harrisonburg_day[i-3]+Harrisonburg_day[i-2]+Harrisonburg_day[i-1]+Harrisonburg_day[i])
            seven_day_H.append(seven_day_sumH)

    seven_max_R = max(seven_day_R) #take the max to find which period was the worst
    seven_max_H = max(seven_day_H)

    seven_max_indexR = seven_day_R.index(seven_max_R) #find the index of this period
    seven_max_indexH = seven_day_H.index(seven_max_H)

    #using the same index from the worst seven day period for the date list to find the start date and then add six to it to find the end date
    print(f"The worst seven day period in Rockingham county was from {R_dates[seven_max_indexR]} to {R_dates[seven_max_indexR+6]}")
    print( f"The worst seven day period in Harrisonburg was from {H_dates[seven_max_indexH]} to {H_dates[seven_max_indexH + 6]}")
    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    for (date, county, state, cases, deaths) in data:
        """print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?"""
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


