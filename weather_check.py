import csv
# Open the database
# The file will be read with header as keys that correspond to each value
my_file = "weather.csv"

def read_csv():
    '''() -> (list(header), list(database))

    Given a csv file, open and read the file.
    Return sorted database:
    - The data categories at row 0 of the file is the header
    - Row 1 and onwards is the database

    REQ: file has to be a valid .csv file with data categories
    '''
    # Open the file given so we can read its content
    with open(my_file, "r") as csv_file:
        # Read the file
        csv_reader = csv.reader(csv_file)
        database = list(csv_reader)
        # File sorted with header as a list
        # Database as a list containing sublists each represent row in file
    return (database[0], database[1:])


def get_temp(year, month, day):
    '''(int, int, int) -> str(min_temp, max_temp)

    Enter a date and return the maximum and minimum temperature values as
    a string.

    REQ: inputs must be valid and from the same row of database
    REQ: outputs must be valid and from the same row of database

    >>> get_temp(2019, 10, 31)
    'Min temp: -5.8 celsius', 'Max temp: 2.1 celsius'
    >>> get_temp(2019, 11, 1)
    'Min temp: -4 celsius', 'Max temp: 2 celsius'
    >>> get_temp(2019, 11, 11)
    'Min temp: -19.4 celsius', 'Max temp: -10.4 celsius'
    >>> get_temp(2019, 7, 12)
    'Temperature data not available'
    '''
    database = read_csv()[1]
    # Find the sublist containing the input values
    for data in database:
        if int(data[0]) == int(year) and int(data[1]) == int(month) and int(data[2]) == int(day):
            # If the value is not given in the database
            if data[3] == "" or data[4] == "":
                return ("Temperature data not available")
            # If we find the input values in database, get the temperature values,
            # and return them.
            else:
                return ("Min temp: " + data[4] + " celsius " + "," " Max temp: " + data[3] + " celsius")


def avg_temp(year, month, day):
    '''(int, int, int) -> str
    Enter a date and return the average temperature of the day in a string.

    REQ: inputs and output must be valid

    >>> avg_temp (2019, 10, 1)
    'Average temperature: 5.74 celsius'
    '''
    database = read_csv()[1]
    mean_temp = []
    # Set the length of the database that will be read to 7
    len(database) == 7
    # index will represent the position of the sublist inside the database list
    index = 0
    # Set a while loop that will read through 7 rows
    while(index < len(database)):
        data = database[index]
        # Check that we find the right values for our inputs
        if int(data[0]) == int(year) and int(data[1]) == int(month) and int(data[2]) == int(day):
            # Take out the max and min values from each of the 7 sublists
            for count in range(0, 7, 1):
                # If the value is not given in the database, set it to 0
                if database[index + count][4] == "":
                    database[index + count][4] = 0
                min_temp = float(database[index + count][4])
                if database[index + count][3] == "":
                    database[index + count][3] = 0
                max_temp = float(database[index + count][3])
                # Calculate the mean of the max and min values
                temp_data = (max_temp + min_temp) / 2
                # Store the mean value into an empty list: mean_temp[]
                mean_temp.append(temp_data)
            return ("Average temperature: " + str(round((sum(mean_temp) / 7), 2)) + " celsius")
        # After the mean value is stored in the list, jump to the next sublist
        # and repeat the process
        index += 1


def get_rain(year, month, day):
    '''(int, int, int) -> str

    Enter a date and return the precipitation value in a string.

    REQ: inputs must be valid and from the same row of the database
    REQ: output must be valid

    >>> get_rain(2019, 10, 9)
    'Total precipitation: 1.5 mm'
    '''
    database = read_csv()[1]
    # Get the sublist where inputs are found
    # Check that we find the right values for our inputs
    for data in database:
        if int(data[0]) == int(year) and int(data[1]) == int(month) and int(data[2]) == int(day):
            # If the value is not given in the database
            if data[5] == "":
                return ("Precipitation data not available")
            # If we find the input values in database, get the temperature values,
            # and return them.
            else:
                return ("Total precipitation: " + data[5] + " mm")


def avg_rain(year, month, day):
    '''(int, int, int) -> str
    Enter a date and return the average precipitation in the next 7 days
    including the input date's values in a string.

    REQ: inputs and output must be valid

    >>> avg_rain (2019, 10, 25)
    'Average precipitation: 0.44 mm'
    '''
    database = read_csv()[1]
    mean_rain = []
    # Set the length of the database that will be read to 7
    len(database) == 7
    # index will represent the position of the sublist inside the database list
    index = 0
    # Set a while loop that will read through 7 rows
    while(index < len(database)):
        data = database[index]
        if int(data[0]) == int(year) and int(data[1]) == int(month) and int(data[2]) == int(day):
            for count in range(0, 7, 1):
                if database[index + count][5] == "":
                    database[index + count][5] = 0
                rain_data = float(database[index + count][5])
                mean_rain.append(rain_data)
            return ("Average precipitation: " + str(round((sum(mean_rain) / 7), 2)) + " mm")
        index += 1


def get_weather(year, month, day):
    '''(int, int, int) -> str
    Enter a date and return the weather description and clothing suggestions for
    that day as a string.

    REQ: inputs and outputs must be valid

    >>> get_weather(2019, 11, 3)
    'Clothing suggestion(s) and weather: boots and coat, snow'
    >>> get_weather(2019, 7, 25)
    'Weather data not available'
    '''
    database = read_csv()[1]
    for data in database:
        if int(data[0]) == int(year) and int(data[1]) == int(month) and int(data[2]) == int(day):
            # When the value is not given in the database
            if data[4] == "" or data[3] == "":
                return("Weather data not available")
            # When the value is not given but since the wind speed and
            # precipitation value have little impact on the outputs in this
            # function, we decided to simply set them to 0 when not given.
            if data[6] == "" or data[5] == "":
                data[6] = 0
                data[5] = 0
            # Set the weather conditions and temperature ranges to variables so
            # it's easier to read through the codes
            temp = float(float(data[3]) + float(data[4])) / 2
            rain = float(data[5]) > 0
            windy = float(data[6]) > 50
            cold_temp = temp < 0
            mod_temp = 0 <= temp <= 20
            warm_temp = temp > 20
            s = "Clothing suggestion(s) and weather: "
            if cold_temp:
                if rain and not windy:
                    return(s + "boots and coat, snow, cold temp")
                elif windy and not rain:
                    return(s + "coat, windy, cold temp")
                elif windy and rain:
                    return(s + "boots and coat, snowstorm, cold temp")
                else:
                    return(s + "coat, cold temp")
            if mod_temp:
                if rain and not windy:
                    return(s + "raincoat or umbrella, rain, moderate temp")
                elif windy and not rain:
                    return(s + "windbreaker, windy, moderate temp")
                elif windy and rain:
                    return(s + "windbreaker and umbrella, windy and rain, moderate temp")
                else:
                    return(s + "jacket, moderate temp")
            if warm_temp:
                if rain and not windy:
                    return(s + "umbrella, rain, warm temp")
                elif windy and not rain:
                    return(s + "windbreaker, windy, warm temp")
                elif windy and rain:
                    return(s + "windbreaker and umbrella, windy and rain, warm temp")
                else:
                    return(s + "t-shirt, warm temp")

# Find the global code below:
# Read the data
csv_header, csv_database = read_csv()
# Print the header and keep it separate from the database.
print(csv_header)
# Print the database:
# The database is a list inside a list: every item of the database list
# represent a row
# Every row is also represented by a list, where the order of the elements
# equals the order of the database headers
print(csv_database)
