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
        "hours": None,
        "minutes": start_time_obj["minutes"] + duration_time_obj["minutes"],
        "time_of_day": start_time_obj["time_of_day"],
        "day": day if day != None else "",
        "days_apart": ""
    }

    twenty_four_hour_format = (
        am_to_24hr_conversion[0] if start_time_obj["time_of_day"] == "AM" and start_time_obj["hours"] == 12 else 
        am_to_24hr_conversion[0 + start_time_obj["hours"]] if start_time_obj["time_of_day"] == "AM" and start_time_obj["hours"] in am_to_24hr_conversion else

        pm_to_24hr_conversion[0] if start_time_obj["hours"] == 12 and start_time_obj["time_of_day"] == "PM" else
        pm_to_24hr_conversion[0 + start_time_obj["hours"]] if pm_to_24hr_conversion[0 + start_time_obj["hours"]] in pm_to_24hr_conversion else
        False
    ) 
    print(twenty_four_hour_format)
    if twenty_four_hour_format == False:
        return "Start time must follow 12 hour format"
    
    calculated_time_obj["hours"] = twenty_four_hour_format
    
    
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)