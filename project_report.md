# CSCA20 Project Report

## Team

--------

**Team Member A** 
- First Name: Kaiwen
- Last Name: Niu
- Student Number: 1005985043
- UofT E-mail Address: kaiwen.niu@mail.utoronto.ca

**Team Member B**  
- First Name: Ruisi Rachel
- Last Name: Li
- Student Number: 1005508372
- UofT E-mail Address: ruisi.li@mail.utoronto.ca

## Project Plan

--------

### Project Title: Weather Checker

### Description

We will write a Python code that returns weather data of a specific date. 
The code will consist of multiple functions and importing database files.
We might also try to find a way to graph the averages.
It will be able to return:
- daily temperature and precipitation
- average temperature and precipitation in the next 7 days
- weather description and recommended clothing 

### Week 1 Plan

**Before** the first tutorial will have:

- Find a good weather database online:
- Write down a list of functions that we need

**After** the first tutorial will have:

- Writing up all required functions with docstrings:
  - Read csv file
  - Get daily maximum and minimum temperature values
  - Get daily precipitation value
  - Calculate mean temperature of the day
        - Calculate the average temperature in the next 7 days
  - Calculate average precipitation
  - Get daily weather description and clothing suggestion 

What is your backup plan if things don’t work out as planned?

- Consult TA or professor for other possibilities of writing the code and maybe focus on the reply functions first
- Not implementing the graphing function 

## Weekly Reports

-----------------

### Week 1 Report

After planning, we wrote down all the requirments and comments for our project so that it could be easier to read and think. Together, we boakdown our project step by step and we also finished both (get_temp) and (get_rain) function smoothly. 

Although we were able to write code for most of the functions, we were struggling on writing codes for the (get_avg_temp) and (get_avg_rain) functions. We decided to move on to the backup plan by not implementing the graphing options, and asking for help from TAs and professor Brian on coding for the two functions.

### Final Week Report

Though our team has only two members, we gathered together and decided to keep as much of our first plan in order to maintain a higher level of ambition for our project.

One of the member emailed TA for suggestions, we got some very helpful information on iterating over a list. However, we still could not get the function work like we want it to be. Eventually, we reached out to professor Brain and asked for further help. Luckily, he gave us a key suggestion of indexing each sublist inside the database list and we were able to get the (avg_temp) and (avg_rain) function to run successfully.

We were able to complete out project prior to our Wednesday tutorial as planned.

## References
-------------

lab8:
- https://uoft.me/a20-lab8

- Lines 1， 6-23， 211-221 are *not* our work.
- Lines 26-54， 96-118 were implemented by us, but designed by CSCA20's lab8 creator.

weather database:
- https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=10666&timeframe=2&StartYear=1840&EndYear=2019&Day=17&Year=2019&Month=10#

## Repo & Video
---------------

Our Python code is uploaded to:
https://github.com/chloe-rachel-csca20/CSCA20-Project

And out video is at:
https://youtu.be/JXYdvMXte74
