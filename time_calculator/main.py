# Michael LaLonde

# Write a function named add_time that takes in two required parameters and one optional parameter:
#   -  a start time in the 12-hour clock format (ending in AM or PM)
#   -  a duration time that indicates the number of hours and minutes
#   -  (optional) a starting day of the week, case insensitive
#
# The function should add the duration time to the start time and return the result.
#
# If the result will be the next day, it should show (next day) after the time.
# If the result will be more than one day later, it should show (n days later) after the time,
# where "n" is the number of days later.
#
# If the function is given the optional starting day of the week parameter,
# then the output should display the day of the week of the result.
# The day of the week in the output should appear after the time and before the number of days later.
#
# Below are some examples of different cases the function should handle.
# Pay close attention to the spacing and punctuation of the results.

def add_time(start, duration, day=None):
    # days of the week in a list
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    new_time = ""

    # split the time section and am/pm section
    time = start.split()

    # get whether the time is AM/PM
    am_pm = time[1]

    # split the actual time up so you can get the hour and minute
    time_split = time[0].split(":")
    hour = time_split[0]
    minute = time_split[1]

    # turn duration into a list and then get the duration hour and minute from the list
    semicolon_index = duration.index(":")
    dur_hour = duration[:semicolon_index]
    dur_minute = duration[semicolon_index + 1:]

    # CALCULATING TIME
    added_hours_from_minutes = 0

    # add the minutes from duration to start minutes
    new_minute = int(minute) + int(dur_minute)
    # for all the times that new_minute is > 60, subtract 60 and add 1 to added_hours_from_minutes
    while (new_minute / 60) >= 1:
        new_minute -= 60
        added_hours_from_minutes += 1

    # get the new amount of hours from
    new_hour = int(hour) + int(dur_hour) + added_hours_from_minutes

    new_am_pm = am_pm
    # number of times the AM and PM changes
    div_by_12 = 0
    while (new_hour / 12) >= 1:
        new_hour -= 12
        if new_am_pm == "AM":
            new_am_pm = "PM"
        else:
            new_am_pm = "AM"
        div_by_12 += 1

    added_days = div_by_12 // 2

    if am_pm == "PM":
        # time started at PM and a PM to AM change happened -> add an extra day
        if div_by_12 % 2 == 1:
            added_days += 1

    # get what the new time would like on the clock if the hours went past 12 or if the
    if new_hour == 0:
        new_hour = 12

    # put the new hour and new minute
    new_time += str(new_hour) + ":"
    if new_minute < 10:  # adds a zero so a 2 would appear as 02
        new_time += "0"
    new_time += str(new_minute)

    # add the AM or PM ot the new_time
    new_time += " " + new_am_pm

    # add the day or newly_calculated day to the new_time
    # if a day was included as a parameter
    if day is not None:
        # fix the day input and get its position in the days list
        day = day.capitalize()
        if added_days != 0:
            # get what the current index of the day of the week is
            start_day_index = days.index(day)
            # the new day of the week is the current index plus the amount of days added modulo 7
            new_day_index = (start_day_index + added_days) % 7
            # get the new day of the week string
            new_day = days[new_day_index]
            new_time += ", " + new_day
        else:  # if no days were added, print the original day
            new_time += ", " + day

    # include the number of days passed to the string
    if added_days >= 1:
        if added_days == 1:
            new_time += " (next day)"
        elif added_days > 1:
            new_time += " (" + str(added_days) + " days later)"
    # return the new time string
    return new_time


def main():
    time = add_time("2:59 PM", "3:11")
    # Returns: 6:10 PM
    print(time)

    time = add_time("11:30 AM", "2:32", "Monday")
    # Returns: 2:02 PM, Monday
    print(time)

    time = add_time("11:43 AM", "00:20")
    # Returns: 12:03 PM
    print(time)

    time = add_time("10:10 PM", "3:30")
    # Returns: 1:40 AM (next day)
    print(time)

    time = add_time("11:43 PM", "24:20", "tueSday")
    # Returns: 12:03 AM, Thursday (2 days later)
    print(time)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
