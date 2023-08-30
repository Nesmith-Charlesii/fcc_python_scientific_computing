def add_time(start_time, duration, day = None):

    def split_time(time):
        
        time_obj = {
            "hours": None,
            "minutes": None,
            "time_of_day": None,
        }

        split_time = time.split(":")
        time_obj["hours"] = int(split_time[0])
        
        if "AM" in split_time[1] or "PM" in split_time[1]:
            minutes = split_time[1].split(" ")[0]
            time_of_day = split_time[1].split(" ")[1]

            time_obj["minutes"] = int(minutes)
            time_obj["time_of_day"] = time_of_day
        else:
            time_obj["minutes"] = int(split_time[1])

        return time_obj
    
    start_time_obj = split_time(start_time)
    duration_time_obj = split_time(duration)
    
    am_to_24hr_conversion = range(0,12)
    pm_to_24hr_conversion = range(12,24)

    calculated_time_obj = {
        "hours": int(),
        "minutes": start_time_obj["minutes"] + duration_time_obj["minutes"],
        "time_of_day": start_time_obj["time_of_day"],
        "day": day,
        "days_apart": int()
    }

    twenty_four_hour_format = (
        am_to_24hr_conversion[0] if start_time_obj["time_of_day"] == "AM" and start_time_obj["hours"] == 12 else 
        am_to_24hr_conversion[0 + start_time_obj["hours"]] if start_time_obj["time_of_day"] == "AM" and start_time_obj["hours"] in am_to_24hr_conversion else

        pm_to_24hr_conversion[0] if start_time_obj["hours"] == 12 and start_time_obj["time_of_day"] == "PM" else
        pm_to_24hr_conversion[0 + start_time_obj["hours"]] if pm_to_24hr_conversion[0 + start_time_obj["hours"]] in pm_to_24hr_conversion else
        False
    ) 

    if twenty_four_hour_format == False:
        return "Start time must follow 12 hour format"
    
    calculated_time_obj["hours"] = (twenty_four_hour_format + duration_time_obj["hours"]) % 24

    if calculated_time_obj["minutes"] >= 60:
        calculated_time_obj["minutes"] = calculated_time_obj["minutes"] - 60
        calculated_time_obj["hours"] += 1

    if calculated_time_obj["hours"] in pm_to_24hr_conversion:
        calculated_time_obj["time_of_day"] = "PM"
    elif calculated_time_obj["hours"] in am_to_24hr_conversion or calculated_time_obj["hours"] == 24:
        calculated_time_obj["time_of_day"] = "AM"
    
    calculated_time_obj["days_apart"] = (
        duration_time_obj["hours"] // 12 if duration_time_obj["hours"] >= 24 else 
        1 if duration_time_obj["hours"] // 12 == 1 else
        calculated_time_obj["days_apart"]
    )

    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    if day != None:
        if calculated_time_obj["days_apart"] < 1:
            calculated_time_obj["day"] = day
        else:
            day_index = days.index(day.lower())
            calculated_day_index = day_index + calculated_time_obj["days_apart"]
            calculated_time_obj["day"] = (
                days[calculated_day_index] if calculated_day_index < len(days) else
                days[calculated_day_index - len(days)]
            )

    if calculated_time_obj["hours"] > 12:
        calculated_time_obj["hours"] = calculated_time_obj["hours"] - 12

    print(f'{calculated_time_obj["hours"]}:{calculated_time_obj["minutes"]:02d} {calculated_time_obj["time_of_day"]}{"," + " " + calculated_time_obj["day"].capitalize() if calculated_time_obj["day"] != None else " "} {"(" + str(calculated_time_obj["days_apart"]) + " days later)" if calculated_time_obj["days_apart"] > 1 else "next day" if calculated_time_obj["days_apart"] == 1 else ""}')
    
    
#add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

#add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

#add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

#add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)