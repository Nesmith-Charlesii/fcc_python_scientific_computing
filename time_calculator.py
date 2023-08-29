def add_time(start_time, duration, day = None):
    # To-do: Convert time to 24 format and change name of function to 24hr_format
    def twenty_four_hour_format(time):
        am_to_24hr_conversion = range(0,12)
        pm_to_24hr_conversion = range(12,24)

        time_obj = {
            "hour": None,
            "minute": None,
            "time_of_day": None,
        }

        split_time = time.split(":")
        time_obj["hour"] = int(split_time[0])
        
        if "AM" in split_time[1] or "PM" in split_time[1]:
            minutes = split_time[1].split(" ")[0]
            time_of_day = split_time[1].split(" ")[1]

            time_obj["minute"] = int(minutes)
            time_obj["time_of_day"] = time_of_day
        else:
            time_obj["minute"] = int(split_time[1])

        time_obj["hour"] = (
            am_to_24hr_conversion[0] if time_obj["hour"] == 12 and time_obj["time_of_day"] == "AM" else 
            am_to_24hr_conversion[0 + time_obj["hour"]] if time_obj["time_of_day"] == "AM" and time_obj["hour"] in am_to_24hr_conversion else

            pm_to_24hr_conversion[0] if time_obj["hour"] == 12 and time_obj["time_of_day"] == "PM" else
            pm_to_24hr_conversion[0 + time_obj["hour"]]
        ) 
        
        # return time_obj
        
    
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

#add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

#add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

#add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

#add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

#add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)