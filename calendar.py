#sim/local/days

day = 212

while day <= 0:
    day += 365

while day >= 365:
    day -= 365

if day >= 0 and day <= 30:
    month = 1
    dayInMonth = day
elif day >= 31 and day <= 58:
    month = 2
    dayInMonth = day - 30
elif day >= 59 and day <= 89:
    month = 3
    dayInMonth = day - 59
elif day >= 90 and day <= 119:
    month = 4
    dayInMonth = day - 89
elif day >= 120 and day <= 150:
    month = 5
    dayInMonth = day - 119
elif day >= 151 and day <= 180:
    month = 6
    dayInMonth = day - 150
elif day >= 181 and day <= 211:
    month = 7
    dayInMonth = day - 180
elif day >= 212 and day <= 242:
    month = 8
    dayInMonth = day - 211
elif day >= 243 and day <= 272:
    month = 9
    dayInMonth = day - 242
elif day >= 273 and day <= 303:
    month = 10
    dayInMonth = day - 272
elif day >= 304 and day <= 333:
    month = 11
    dayInMonth = day - 303
elif day >= 334 and day <= 364:
    month = 12
    dayInMonth = day - 333
else:
    month = "e"

if dayInMonth >= 1 and dayInMonth <= 9:
    dayInMonthFirstDigit = 0
    dayInMonthSecondDigit = dayInMonth
elif dayInMonth >= 10 and dayInMonth <= 19:
    dayInMonthFirstDigit = 1
    dayInMonthSecondDigit = dayInMonth - 10
elif dayInMonth >= 20 and dayInMonth <= 29:
    dayInMonthFirstDigit = 2
    dayInMonthSecondDigit = dayInMonth - 20
else:
    dayInMonthFirstDigit = 3
    dayInMonthSecondDigit = dayInMonth - 30




#sim/weather/temperature_ambient_c

temperature = 21.22258
temperature = round(temperature)
temperature = str(temperature)
temperature = temperature + "°"




#sim/cockpit2/clock_timer/local_time_hours
hours = 15
#sim/cockpit2/clock_timer/local_time_minutes
minutes = 0


if hours >= 0 and hours <= 9:
    hoursFirstDigit = 0
    hoursSecondDigit = hours
elif hours >= 10 and hours <= 19:
    hoursFirstDigit = 1
    hoursSecondDigit = hours - 10
elif hours >= 20 and hours <= 23:
    hoursFirstDigit = 20
    hoursSecondDigit = hours - 20
else:
    hoursFirstDigit = 0
    hoursSecondDigit = 0


if minutes >= 0 and minutes <= 9:
    minutesFirstDigit = 0
    minutesSecondDigit = minutes
elif minutes >= 10 and minutes <= 19:
    minutesFirstDigit = 1
    minutesSecondDigit = minutes - 10
elif minutes >= 20 and minutes <= 29:
    minutesFirstDigit = 2
    minutesSecondDigit = minutes - 20
elif minutes >= 30 and minutes <= 39:
    minutesFirstDigit = 3
    minutesSecondDigit = minutes - 30
elif minutes >= 40 and minutes <= 49:
    minutesFirstDigit = 4
    minutesSecondDigit = minutes - 40
elif minutes >= 50 and minutes <= 59:
    minutesFirstDigit = 5
    minutesSecondDigit = minutes - 50
else:
    minutesFirstDigit = 0
    minutesSecondDigit = 0


#print(month)
#print(dayInMonth)
#print(temperature)

print(str(dayInMonthFirstDigit) + str(dayInMonthSecondDigit) + ". " + str(month) + ".  " + str(hoursFirstDigit) + str(hoursSecondDigit) + ":" + str(minutesFirstDigit) + str(minutesSecondDigit) + "  " + str(temperature))

